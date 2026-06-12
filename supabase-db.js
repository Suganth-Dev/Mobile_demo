// ============================================================
// MTS Connect — Supabase Database Layer (supabase-db.js)
// Shared by Learning_app and mobile_app
// Replaces localStorage getDb()/saveDb() / getDB()/saveDB()
// ============================================================

const SUPABASE_URL = 'https://woznrvhbckvttwjwailg.supabase.co';
const SUPABASE_KEY = 'sb_publishable_ntkgSRWNCG_lraD0KNoF_w_VZImzDUg';

// Initialize Supabase client (works with CDN and module builds)
let supabaseClient;
(function initSupabaseClient() {
  try {
    const factory = (typeof window !== 'undefined' && window.supabase)
      ? window.supabase
      : (typeof supabase !== 'undefined' ? supabase : null);
    if (factory && factory.createClient) {
      supabaseClient = factory.createClient(SUPABASE_URL, SUPABASE_KEY);
    } else {
      console.error('[MTS] Supabase JS library not loaded yet. Add CDN script before supabase-db.js');
    }
  } catch (e) {
    console.error('[MTS] Failed to init Supabase client:', e);
  }
})();

// ─────────────────────────────────────────────────────────────
// IN-MEMORY CACHE (replaces localStorage)
// ─────────────────────────────────────────────────────────────
let _dbCache = null;
let _dbLoaded = false;

// ─────────────────────────────────────────────────────────────
// LOAD ALL DATA FROM SUPABASE (called once on page load)
// ─────────────────────────────────────────────────────────────
async function loadAllFromSupabase() {
  if (!supabaseClient) {
    console.warn('[MTS] Supabase not ready — falling back to seed data');
    _dbCache = JSON.parse(JSON.stringify(typeof InitialSeedData !== 'undefined' ? InitialSeedData : {}));
    _dbLoaded = true;
    return;
  }

  try {
    const [
      studentsRes, teachersRes, parentsRes, classesRes,
      homeworkRes, submissionsRes, announcementsRes, eventsRes,
      absenceRes, approvalsRes, auditRes, statusRes,
      sessionsRes, messagesRes, ptBookingRes, ptSlotsRes
    ] = await Promise.all([
      supabaseClient.from('students').select('*').order('created_at'),
      supabaseClient.from('teachers').select('*').order('created_at'),
      supabaseClient.from('parents').select('*').order('created_at'),
      supabaseClient.from('classes').select('*'),
      supabaseClient.from('homework').select('*').order('created_at', { ascending: false }),
      supabaseClient.from('submissions').select('*').order('created_at', { ascending: false }),
      supabaseClient.from('announcements').select('*').order('created_at', { ascending: false }),
      supabaseClient.from('events').select('*').order('created_at'),
      supabaseClient.from('absence_reports').select('*').order('created_at', { ascending: false }),
      supabaseClient.from('approvals').select('*').order('created_at', { ascending: false }),
      supabaseClient.from('audit_logs').select('*').order('created_at', { ascending: false }),
      supabaseClient.from('school_status').select('*').eq('id', 1).single(),
      supabaseClient.from('sessions').select('*'),
      supabaseClient.from('messages').select('*').order('created_at'),
      supabaseClient.from('pt_bookings').select('*').eq('parent_email','parent@mts.edu').order('booked_at', { ascending: false }).limit(1).maybeSingle(),
      supabaseClient.from('pt_slots').select('*').order('id'),
    ]);

    const homeworkMapped = (homeworkRes.data   || []).map(mapHomework);
    const submissionsMapped = (submissionsRes.data|| []).map(mapSubmission);

    // Link submissions dynamically to matching homework title context
    homeworkMapped.forEach(hw => {
      hw.submissions = submissionsMapped.filter(s => s.assignment === hw.title);
    });

    _dbCache = {
      // --- SHARED DATA ---
      students:       (studentsRes.data   || []).map(mapStudent),
      teachers:       (teachersRes.data   || []).map(mapTeacher),
      parents:        (parentsRes.data    || []).map(mapParent),
      classes:        (classesRes.data    || []).map(mapClass),
      homework:       homeworkMapped,
      submissions:    submissionsMapped,
      announcements:  (announcementsRes.data || []).map(mapAnnouncement),
      events:         (eventsRes.data     || []).map(mapEvent),
      absenceReports: (absenceRes.data    || []).map(mapAbsenceReport),
      absenceLogs:    (absenceRes.data    || []).map(mapAbsenceLog),
      approvals:      (approvalsRes.data  || []).map(mapApproval),
      auditLog:       (auditRes.data      || []).map(mapAuditLog),
      auditLogs:      (auditRes.data      || []).map(mapAuditLogMobile),
      schoolStatus:   mapSchoolStatus(statusRes.data),
      sessions:       (sessionsRes.data   || []).map(mapSession),
      messages:       groupMessagesByThread(messagesRes.data || []),
      chatLogs:       (messagesRes.data   || []).filter(m => m.sender).map(mapChatLog),
      ptSlots:        (ptSlotsRes.data    || []).map(mapPtSlot),
      bookedPtSlot:   ptBookingRes.data ? ptBookingRes.data.slot : null,

      // --- STATE FLAGS ---
      currentUser:    null,
      currentLanguage:'en',
      activeChild:    'Anika Kumar',
      version:        'mts_mobile_v1.0.4',

      // --- PREFERENCES ---
      notificationMatrix: {
        announcements: { push: true,  email: true,  inapp: true, wa: false },
        homework:      { push: true,  email: false, inapp: true, wa: false },
        attendance:    { push: true,  email: true,  inapp: true, wa: true  },
        messages:      { push: true,  email: false, inapp: true, wa: false }
      },
      parentChecklist: { tuition: true, medical: false, photo: true },
    };

    _dbLoaded = true;
    console.log('[MTS] ✅ Supabase data loaded successfully');

  } catch (err) {
    console.error('[MTS] ❌ Failed to load from Supabase:', err);
    // Fallback to seed data so UI doesn't break
    if (typeof InitialSeedData !== 'undefined') {
      _dbCache = JSON.parse(JSON.stringify(InitialSeedData));
    }
    _dbLoaded = true;
  }
}

// ─────────────────────────────────────────────────────────────
// GETDB / SAVEDB — Drop-in replacements (sync, uses cache)
// ─────────────────────────────────────────────────────────────
function getDb()  { return _dbCache; }
function saveDb(db) { _dbCache = db; }
function getDB()  { return _dbCache; }
function saveDB(data) { _dbCache = data; }

// ─────────────────────────────────────────────────────────────
// MAPPER FUNCTIONS: Supabase row → JS object (snake → camel)
// ─────────────────────────────────────────────────────────────
function mapStudent(r) {
  return {
    id:           r.id,
    name:         r.name,
    tamilName:    r.tamil_name,
    grade:        r.grade,
    section:      r.section || r.class,
    class:        r.class   || r.section,
    itaId:        r.ita_id,
    ita:          r.ita     || r.ita_id,
    guardian:     r.guardian,
    status:       r.status,
    dob:          r.dob,
    enrollDate:   r.enroll_date,
    phone:        r.phone,
    notes:        r.notes,
    photoConsent: r.photo_consent,
    medicalForm:  r.medical_form,
  };
}

function mapTeacher(r) {
  return {
    id:       r.teacher_id,
    email:    r.email,
    name:     r.name,
    role:     r.role,
    initials: r.initials,
    grades:   r.grades,
    phone:    r.phone,
    class:    r.class,
    subject:  r.subject,
    status:   r.status,
    password: r.password,
  };
}

function mapParent(r) {
  return {
    id:       r.parent_id,
    email:    r.email,
    name:     r.name,
    role:     r.role || 'Parent',
    initials: r.initials,
    phone:    r.phone,
    children: r.children || [],
    student:  r.student,
    relation: r.relation || 'Parent',
    status:   r.status || 'active',
    password: r.password,
  };
}

function mapClass(r) {
  return {
    id:              r.id,
    name:            r.name || r.code,
    code:            r.code || r.name,
    teacher:         r.teacher_name,
    studentCount:    r.student_count,
    students:        r.student_count,
    lastAttendance:  r.last_attendance,
    status:          r.status,
  };
}

function mapHomework(r) {
  return {
    id:          r.id,
    title:       r.title,
    titleTa:     r.title_ta,
    classCode:   r.class_code,
    grade:       r.grade,
    due:         r.due_date,
    dueDate:     r.due_date,
    desc:        r.description,
    description: r.description,
    status:      r.status,
    fileUrl:     r.file_url,
    stats: {
      submitted: r.stat_submitted || 0,
      approved:  r.stat_approved  || 0,
      pending:   r.stat_pending   || 0,
      overdue:   r.stat_overdue   || 0,
    },
    submissions: [], // loaded separately when needed
  };
}

function mapSubmission(r) {
  return {
    id:           r.id,
    student:      r.student_name,
    studentName:  r.student_name,
    assignment:   r.assignment_title,
    date:         r.submitted_at,
    file:         r.file_name,
    attachment:   r.file_name,
    fileType:     r.file_type,
    textNotes:    r.text_notes,
    status:       r.status,
    comment:      r.comment || '',
    gradeGiven:   r.grade_given || '',
    fileUrl:      r.file_url,
    evaluation:   { grade: r.grade_given || '', comment: r.comment || '' },
  };
}

function mapAnnouncement(r) {
  return {
    id:           r.id,
    priority:     r.priority,
    badge:        r.badge,
    title:        r.title,
    titleTa:      r.title_ta,
    body:         r.body,
    bodyTa:       r.body_ta,
    date:         r.date,
    audience:     r.audience,
    ackRequired:  r.ack_required,
    acknowledged: r.acknowledged || [],
    desc:         r.description || r.body,
    acknowledgedBy: r.acknowledged || [],
  };
}

function mapEvent(r) {
  return {
    id:         r.id,
    name:       r.name || r.title,
    title:      r.title || r.name,
    date:       r.date,
    time:       r.time,
    type:       r.type,
    location:   r.location,
    audience:   r.audience,
    capacity:   r.capacity,
    rsvps:      { yes: r.rsvp_yes || 0, no: r.rsvp_no || 0 },
    rsvpStatus: r.rsvp_status || {},
    status:     r.status,
  };
}

function mapAbsenceReport(r) {
  return {
    student:  r.student_name,
    date:     r.date,
    reason:   r.reason,
    notes:    r.notes,
    status:   r.status,
  };
}

function mapAbsenceLog(r) {
  return {
    id:          r.absence_id || r.id,
    studentName: r.student_name,
    date:        r.date,
    reason:      r.reason,
    notes:       r.notes,
    status:      r.status,
  };
}

function mapApproval(r) {
  return {
    id:       r.id,
    category: r.category,
    type:     r.type,
    user:     r.user_name,
    details:  r.details,
    targetId: r.target_id,
    date:     r.date,
    status:   r.status,
  };
}

function mapAuditLog(r) {
  return {
    timestamp: r.timestamp,
    user:      r.user,
    action:    r.action,
    target:    r.target,
    details:   r.details,
    ip:        r.ip,
  };
}

function mapAuditLogMobile(r) {
  return {
    id:        r.audit_id || r.id,
    timestamp: r.timestamp,
    user:      r.user,
    action:    r.action,
    target:    r.target,
    details:   r.details,
    ip:        r.ip,
  };
}

function mapSchoolStatus(r) {
  if (!r) return {
    status: 'green', statusText: '✅ CLASS ON',
    statusTextTa: '✅ வகுப்பு நடைபெறும்',
    venue: 'MTS Building A', parking: 'Main Lot Open',
    note: 'Friday drop-off zones active at 6:00 PM.'
  };
  return {
    status:       r.status,
    statusText:   r.status_text,
    statusTextTa: r.status_text_ta,
    venue:        r.venue,
    parking:      r.parking,
    note:         r.note,
  };
}

function mapSession(r) {
  return {
    id:      r.id,
    user:    r.user_label,
    device:  r.device,
    ip:      r.ip,
    time:    r.time,
    current: r.is_current,
  };
}

function groupMessagesByThread(rows) {
  const result = {};
  rows.filter(r => r.thread_id).forEach(r => {
    if (!result[r.thread_id]) result[r.thread_id] = [];
    result[r.thread_id].push({ type: r.type, text: r.text, time: r.time });
  });
  return result;
}

function mapChatLog(r) {
  return {
    sender:   r.sender,
    role:     r.role,
    receiver: r.receiver,
    text:     r.text,
    time:     r.time,
  };
}

function mapPtSlot(r) {
  return {
    id:       r.id,
    time:     r.time,
    status:   r.status,
    bookedBy: r.booked_by,
  };
}

// ─────────────────────────────────────────────────────────────
// SUPABASE WRITE FUNCTIONS (called by each CRUD operation)
// ─────────────────────────────────────────────────────────────

// ── STUDENTS ─────────────────────────────────────────────────
async function sbAddStudent(s) {
  // Sync to parent children array in-memory immediately for instant UI update
  if (_dbCache && _dbCache.parents && s.guardian) {
    const guardianLower = s.guardian.toLowerCase();
    const parent = _dbCache.parents.find(p => p.name.toLowerCase() === guardianLower);
    if (parent) {
      if (!parent.children) parent.children = [];
      if (!parent.children.includes(s.name)) {
        parent.children.push(s.name);
      }
    }
  }

  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('students').insert({
    id: s.id, name: s.name, tamil_name: s.tamilName,
    grade: s.grade, section: s.section, class: s.section,
    ita_id: s.itaId, ita: s.itaId, guardian: s.guardian,
    status: s.status, dob: s.dob, enroll_date: s.enrollDate,
    phone: s.phone, notes: s.notes,
    photo_consent: s.photoConsent || 'Not Selected',
    medical_form: s.medicalForm  || 'Not Selected',
  });
  if (error) {
    console.error('[MTS] sbAddStudent:', error.message);
    return;
  }

  // Sync to parent children array in Supabase
  if (s.guardian) {
    try {
      const { data: parentData, error: parentFetchErr } = await supabaseClient
        .from('parents')
        .select('children, email')
        .ilike('name', s.guardian)
        .maybeSingle();

      if (!parentFetchErr && parentData) {
        let currentChildren = parentData.children || [];
        if (!currentChildren.includes(s.name)) {
          currentChildren.push(s.name);
          const { error: parentUpdateErr } = await supabaseClient
            .from('parents')
            .update({ children: currentChildren })
            .eq('email', parentData.email);
          if (parentUpdateErr) {
            console.error('[MTS] Failed to sync children to parent in Supabase:', parentUpdateErr.message);
          } else {
            console.log('[MTS] Synced child to parent in Supabase successfully');
          }
        }
      }
    } catch (e) {
      console.error('[MTS] Error syncing parent children array in Supabase:', e);
    }
  }
}

async function sbUpdateStudent(s) {
  let oldName = '';
  let oldGuardian = '';

  // Get old details from memory
  if (_dbCache && _dbCache.students) {
    const oldStudent = _dbCache.students.find(st => st.id === s.id);
    if (oldStudent) {
      oldName = oldStudent.name;
      oldGuardian = oldStudent.guardian;
    }
  }

  // Update memory cache parent lists if name or guardian changed
  if (_dbCache && _dbCache.parents) {
    if (oldGuardian && oldGuardian.toLowerCase() !== (s.guardian || '').toLowerCase() && oldName) {
      const oldGuardianLower = oldGuardian.toLowerCase();
      const oldParent = _dbCache.parents.find(p => p.name.toLowerCase() === oldGuardianLower);
      if (oldParent && oldParent.children) {
        oldParent.children = oldParent.children.filter(c => c !== oldName);
      }
    }
    const targetGuardian = s.guardian;
    if (targetGuardian) {
      const targetGuardianLower = targetGuardian.toLowerCase();
      const newParent = _dbCache.parents.find(p => p.name.toLowerCase() === targetGuardianLower);
      if (newParent) {
        if (!newParent.children) newParent.children = [];
        newParent.children = newParent.children.filter(c => c !== oldName);
        if (!newParent.children.includes(s.name)) {
          newParent.children.push(s.name);
        }
      }
    }
  }

  if (!supabaseClient) return;

  const { error } = await supabaseClient.from('students').update({
    name: s.name, tamil_name: s.tamilName, grade: s.grade,
    section: s.section, class: s.section, ita_id: s.itaId, ita: s.itaId,
    guardian: s.guardian, status: s.status, dob: s.dob,
    notes: s.notes, photo_consent: s.photoConsent, medical_form: s.medicalForm,
  }).eq('id', s.id);
  if (error) {
    console.error('[MTS] sbUpdateStudent:', error.message);
    return;
  }

  // Sync to parent children array in Supabase
  try {
    if (oldGuardian && oldGuardian.toLowerCase() !== (s.guardian || '').toLowerCase() && oldName) {
      const { data: oldParentData } = await supabaseClient
        .from('parents')
        .select('children, email')
        .ilike('name', oldGuardian)
        .maybeSingle();
      if (oldParentData && oldParentData.children) {
        const updatedOldChildren = oldParentData.children.filter(c => c !== oldName);
        await supabaseClient
          .from('parents')
          .update({ children: updatedOldChildren })
          .eq('email', oldParentData.email);
      }
    }

    if (s.guardian) {
      const { data: newParentData } = await supabaseClient
        .from('parents')
        .select('children, email')
        .ilike('name', s.guardian)
        .maybeSingle();
      if (newParentData) {
        let currentChildren = newParentData.children || [];
        if (oldName && oldName !== s.name) {
          currentChildren = currentChildren.filter(c => c !== oldName);
        }
        if (!currentChildren.includes(s.name)) {
          currentChildren.push(s.name);
        }
        await supabaseClient
          .from('parents')
          .update({ children: currentChildren })
          .eq('email', newParentData.email);
      }
    }
  } catch (e) {
    console.error('[MTS] Error syncing parent children array on student update:', e);
  }
}

async function sbDeleteStudent(studentId) {
  let studentName = '';
  let guardianName = '';

  if (_dbCache && _dbCache.students) {
    const student = _dbCache.students.find(st => st.id === studentId);
    if (student) {
      studentName = student.name;
      guardianName = student.guardian;
    }
  }

  if (_dbCache && _dbCache.parents && studentName && guardianName) {
    const parent = _dbCache.parents.find(p => p.name === guardianName);
    if (parent && parent.children) {
      parent.children = parent.children.filter(c => c !== studentName);
    }
  }

  if (!supabaseClient) return;

  if (!studentName || !guardianName) {
    try {
      const { data: studentData } = await supabaseClient
        .from('students')
        .select('name, guardian')
        .eq('id', studentId)
        .maybeSingle();
      if (studentData) {
        studentName = studentData.name;
        guardianName = studentData.guardian;
      }
    } catch (e) {
      console.error('[MTS] Error fetching student details before delete:', e);
    }
  }

  const { error } = await supabaseClient.from('students').delete().eq('id', studentId);
  if (error) {
    console.error('[MTS] sbDeleteStudent:', error.message);
    return;
  }

  if (studentName && guardianName) {
    try {
      const { data: parentData, error: parentFetchErr } = await supabaseClient
        .from('parents')
        .select('children, email')
        .eq('name', guardianName)
        .maybeSingle();

      if (!parentFetchErr && parentData && parentData.children) {
        const updatedChildren = parentData.children.filter(c => c !== studentName);
        await supabaseClient
          .from('parents')
          .update({ children: updatedChildren })
          .eq('email', parentData.email);
      }
    } catch (e) {
      console.error('[MTS] Error removing child from parent in Supabase:', e);
    }
  }
}

async function sbUpdateStudentNotes(studentId, notes) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('students').update({ notes }).eq('id', studentId);
  if (error) console.error('[MTS] sbUpdateStudentNotes:', error.message);
}

async function sbUpdateStudentStatus(studentName, status) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('students').update({ status }).eq('name', studentName);
  if (error) console.error('[MTS] sbUpdateStudentStatus:', error.message);
}

// ── TEACHERS ─────────────────────────────────────────────────
async function sbAddTeacher(t) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('teachers').insert({
    teacher_id: t.id, email: t.email, name: t.name,
    role: t.role || 'Teacher', initials: t.initials,
    grades: t.grades, phone: t.phone, class: t.class,
    subject: t.subject, status: t.status || 'active',
    password: t.password || 'teacher123',
  });
  if (error) console.error('[MTS] sbAddTeacher:', error.message);
}

async function sbUpdateTeacher(email, updates) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('teachers').update({
    name: updates.name, role: updates.role, initials: updates.initials,
    grades: updates.grades, phone: updates.phone,
    class: updates.class, subject: updates.subject, status: updates.status,
  }).eq('email', email);
  if (error) console.error('[MTS] sbUpdateTeacher:', error.message);
}

async function sbDeleteTeacher(email) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('teachers').delete().eq('email', email);
  if (error) console.error('[MTS] sbDeleteTeacher:', error.message);
}

// ── PARENTS ──────────────────────────────────────────────────
async function sbAddParent(p) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('parents').insert({
    parent_id: p.id, email: p.email, name: p.name,
    role: p.role || 'Parent', initials: p.initials,
    phone: p.phone, children: p.children || [],
    student: p.student, relation: p.relation || 'Parent',
    status: p.status || 'active',
    password: p.password || 'parent123',
  });
  if (error) console.error('[MTS] sbAddParent:', error.message);
}

async function sbUpdateParent(email, updates) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('parents').update({
    name: updates.name, phone: updates.phone,
    children: updates.children, initials: updates.initials,
    student: updates.student, relation: updates.relation,
  }).eq('email', email);
  if (error) console.error('[MTS] sbUpdateParent:', error.message);
}

async function sbDeleteParent(email) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('parents').delete().eq('email', email);
  if (error) console.error('[MTS] sbDeleteParent:', error.message);
}

// ── HOMEWORK ─────────────────────────────────────────────────
async function sbAddHomework(hw) {
  if (!supabaseClient) return;
  const newId = hw.id || 'hw-' + Date.now().toString().slice(-6);
  const gradeVal = hw.grade || (hw.classCode ? hw.classCode.replace('Grade ', '') : null);
  const { data, error } = await supabaseClient.from('homework').insert({
    id: newId,
    title: hw.title,
    title_ta: hw.titleTa,
    class_code: hw.classCode,
    grade: gradeVal,
    due_date: hw.due || hw.dueDate,
    description: hw.desc || hw.description,
    status: 'Active',
    stat_submitted: 0,
    stat_approved: 0,
    stat_pending: 0,
    stat_overdue: 0,
    file_url: hw.fileUrl || null,
  }).select().single();
  if (error) {
    console.error('[MTS] sbAddHomework error:', error.message);
    throw error;
  }
  return data;
}

async function sbUpdateHomework(hwId, hwUpdates) {
  if (!supabaseClient) return;
  const gradeVal = hwUpdates.grade || (hwUpdates.classCode ? hwUpdates.classCode.replace('Grade ', '') : null);
  
  const payload = {};
  if (hwUpdates.title !== undefined) payload.title = hwUpdates.title;
  if (hwUpdates.titleTa !== undefined) payload.title_ta = hwUpdates.titleTa;
  if (hwUpdates.classCode !== undefined) payload.class_code = hwUpdates.classCode;
  if (gradeVal !== undefined) payload.grade = gradeVal;
  if (hwUpdates.due !== undefined || hwUpdates.dueDate !== undefined) payload.due_date = hwUpdates.due || hwUpdates.dueDate;
  if (hwUpdates.desc !== undefined || hwUpdates.description !== undefined) payload.description = hwUpdates.desc || hwUpdates.description;
  if (hwUpdates.fileUrl !== undefined) payload.file_url = hwUpdates.fileUrl;
  if (hwUpdates.status !== undefined) payload.status = hwUpdates.status;

  const { data, error } = await supabaseClient.from('homework').update(payload).eq('id', hwId).select().single();
  if (error) {
    console.error('[MTS] sbUpdateHomework error:', error.message);
    throw error;
  }
  return data;
}

async function sbDeleteHomework(hwId) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('homework').delete().eq('id', hwId);
  if (error) {
    console.error('[MTS] sbDeleteHomework error:', error.message);
    throw error;
  }
}

async function sbUpdateHomeworkStats(hwId, stats) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('homework').update({
    stat_submitted: stats.submitted, stat_approved: stats.approved,
    stat_pending: stats.pending, stat_overdue: stats.overdue,
  }).eq('id', hwId);
  if (error) console.error('[MTS] sbUpdateHomeworkStats:', error.message);
}

// ── SUBMISSIONS ──────────────────────────────────────────────
async function sbAddSubmission(sub) {
  if (!supabaseClient) return;
  const { data, error } = await supabaseClient.from('submissions').insert({
    homework_id: sub.homework_id || null,
    student_name: sub.student || sub.studentName,
    assignment_title: sub.assignment || sub.assignmentTitle,
    submitted_at: sub.date,
    file_name: sub.file || sub.attachment,
    file_type: sub.fileType || 'document',
    text_notes: sub.textNotes || '',
    status: 'Pending Review',
    comment: sub.comment || '',
    file_url: sub.fileUrl || null,
  }).select().single();
  if (error) console.error('[MTS] sbAddSubmission:', error.message);
  return data;
}

async function sbUpdateSubmission(subId, status, comment, gradeGiven = '') {
  if (!supabaseClient) return;
  const updatePayload = { status, comment };
  if (gradeGiven) {
    updatePayload.grade_given = gradeGiven;
  }
  const { error } = await supabaseClient.from('submissions').update(updatePayload).eq('id', subId);
  if (error) console.error('[MTS] sbUpdateSubmission:', error.message);
}

// ── EXTRA UTILITIES FOR CREDENTIALS & FILE UPLOADS ──────────
async function sbVerifyCredentials(email, password, role) {
  if (!supabaseClient) return null;
  const table = role === 'admin' ? 'admins' : role === 'teacher' ? 'teachers' : 'parents';
  try {
    const { data, error } = await supabaseClient
      .from(table)
      .select('*')
      .eq('email', email)
      .eq('password', password)
      .maybeSingle();

    if (error) {
      console.error('[MTS] sbVerifyCredentials error:', error.message);
      return null;
    }
    return data;
  } catch (e) {
    console.error('[MTS] sbVerifyCredentials exception:', e);
    return null;
  }
}

async function sbUploadFile(file, folderPath = 'uploads') {
  if (!supabaseClient) throw new Error('Supabase client not initialized');
  
  try {
    // Dynamically ensure bucket exists
    const { data: buckets } = await supabaseClient.storage.listBuckets();
    const bucketExists = buckets && buckets.find(b => b.name === 'homework_files');
    if (!bucketExists) {
      await supabaseClient.storage.createBucket('homework_files', { public: true });
    }
  } catch(e) {
    console.error('[MTS] Bucket check/create failed:', e);
  }

  const fileExt = file.name.split('.').pop();
  const fileName = `${Date.now()}_${Math.random().toString(36).substring(2, 8)}.${fileExt}`;
  const filePath = `${folderPath}/${fileName}`;

  const { data, error } = await supabaseClient.storage
    .from('homework_files')
    .upload(filePath, file, { cacheControl: '3600', upsert: true });

  if (error) {
    console.error('[MTS] sbUploadFile error:', error.message);
    throw error;
  }

  const { data: urlData } = supabaseClient.storage
    .from('homework_files')
    .getPublicUrl(filePath);

  return urlData?.publicUrl || '';
}

// ── ANNOUNCEMENTS ────────────────────────────────────────────
async function sbAddAnnouncement(ann) {
  if (!supabaseClient) return;
  const newId = 'ann-' + Date.now().toString().slice(-6);
  const { data, error } = await supabaseClient.from('announcements').insert({
    id: newId, priority: ann.priority, badge: ann.badge,
    title: ann.title, title_ta: ann.titleTa,
    body: ann.body, body_ta: ann.bodyTa,
    date: ann.date, audience: ann.audience,
    ack_required: ann.ackRequired, acknowledged: [],
    desc: ann.body,
  }).select().single();
  if (error) console.error('[MTS] sbAddAnnouncement:', error.message);
  return data;
}

async function sbUpdateAnnouncementAck(annId, acknowledgedList) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('announcements')
    .update({ acknowledged: acknowledgedList, acknowledged_by: acknowledgedList })
    .eq('id', annId);
  if (error) console.error('[MTS] sbUpdateAnnouncementAck:', error.message);
}

// ── EVENTS ───────────────────────────────────────────────────
async function sbAddEvent(ev) {
  if (!supabaseClient) return;
  const newId = 'evt-' + Date.now().toString().slice(-6);
  const { data, error } = await supabaseClient.from('events').insert({
    id: newId, name: ev.name || ev.title, title: ev.title || ev.name,
    date: ev.date, time: ev.time, type: ev.type,
    location: ev.location, audience: ev.audience,
    capacity: parseInt(ev.capacity) || 100,
    rsvp_yes: 0, rsvp_no: 0, rsvp_status: {},
    status: ev.status || 'RSVPs Open',
  }).select().single();
  if (error) console.error('[MTS] sbAddEvent:', error.message);
  return data;
}

async function sbUpdateEventRsvp(eventId, yes, no) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('events')
    .update({ rsvp_yes: yes, rsvp_no: no })
    .eq('id', eventId);
  if (error) console.error('[MTS] sbUpdateEventRsvp:', error.message);
}

async function sbUpdateEventRsvpStatus(eventId, rsvpStatus) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('events')
    .update({ rsvp_status: rsvpStatus })
    .eq('id', eventId);
  if (error) console.error('[MTS] sbUpdateEventRsvpStatus:', error.message);
}

// ── MESSAGES ─────────────────────────────────────────────────
async function sbAddMessage(threadId, message) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('messages').insert({
    thread_id: threadId, type: message.type,
    text: message.text, time: message.time,
  });
  if (error) console.error('[MTS] sbAddMessage:', error.message);
}

async function sbAddChatLog(entry) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('messages').insert({
    sender: entry.sender, role: entry.role,
    receiver: entry.receiver, text: entry.text, time: entry.time,
  });
  if (error) console.error('[MTS] sbAddChatLog:', error.message);
}

// ── ABSENCE REPORTS ──────────────────────────────────────────
async function sbAddAbsenceReport(report) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('absence_reports').insert({
    absence_id: report.id || ('abs-' + Date.now().toString().slice(-6)),
    student_name: report.student || report.studentName,
    parent_email: 'parent@mts.edu',
    date: report.date, reason: report.reason,
    notes: report.notes || '', status: report.status || 'Pending',
  });
  if (error) console.error('[MTS] sbAddAbsenceReport:', error.message);
}

// ── PT BOOKINGS ──────────────────────────────────────────────
async function sbBookPtSlot(slot, parentEmail) {
  if (!supabaseClient) return;
  const email = parentEmail || 'parent@mts.edu';
  await supabaseClient.from('pt_bookings').delete().eq('parent_email', email);
  const { error } = await supabaseClient.from('pt_bookings').insert({
    parent_email: email, slot: slot,
  });
  if (error) console.error('[MTS] sbBookPtSlot:', error.message);
}

async function sbUpdatePtSlot(slotId, status, bookedBy) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('pt_slots')
    .update({ status, booked_by: bookedBy })
    .eq('id', slotId);
  if (error) console.error('[MTS] sbUpdatePtSlot:', error.message);
}

// ── SCHOOL STATUS ────────────────────────────────────────────
async function sbUpdateSchoolStatus(statusObj) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('school_status').update({
    status: statusObj.status, status_text: statusObj.statusText,
    status_text_ta: statusObj.statusTextTa,
    venue: statusObj.venue, parking: statusObj.parking,
    note: statusObj.note, updated_at: new Date().toISOString(),
  }).eq('id', 1);
  if (error) console.error('[MTS] sbUpdateSchoolStatus:', error.message);
}

// ── APPROVALS ────────────────────────────────────────────────
async function sbUpdateApproval(approvalId, newStatus) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('approvals')
    .update({ status: newStatus })
    .eq('id', String(approvalId));
  if (error) console.error('[MTS] sbUpdateApproval:', error.message);
}

// ── AUDIT LOGS ───────────────────────────────────────────────
async function sbAddAuditLog(entry) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('audit_logs').insert({
    audit_id: entry.id || ('aud-' + Date.now().toString().slice(-6)),
    timestamp: entry.timestamp,
    user: entry.user, action: entry.action,
    target: entry.target, details: entry.details,
    ip: entry.ip || 'web-session',
  });
  if (error) console.error('[MTS] sbAddAuditLog:', error.message);
}

// ── SESSIONS ─────────────────────────────────────────────────
async function sbDeleteSession(sessionId) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('sessions').delete().eq('id', String(sessionId));
  if (error) console.error('[MTS] sbDeleteSession:', error.message);
}

// ── ATTENDANCE ───────────────────────────────────────────────
async function sbFinalizeAttendance(classCode, lastAttendanceStr) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('classes')
    .update({ last_attendance: lastAttendanceStr })
    .eq('id', classCode);
  if (error) console.error('[MTS] sbFinalizeAttendance:', error.message);
}

async function sbAddAttendanceRecord(record) {
  if (!supabaseClient) return;
  const { error } = await supabaseClient.from('attendance_records').insert({
    student_id: record.studentId, student_name: record.studentName,
    class_code: record.classCode, session_date: record.sessionDate,
    status: record.status, notes: record.notes || '',
  });
  if (error) console.error('[MTS] sbAddAttendanceRecord:', error.message);
}

// ─────────────────────────────────────────────────────────────
// UTILITY: Timestamp helper
// ─────────────────────────────────────────────────────────────
function sbTimestamp() {
  return new Date().toLocaleDateString([], { month: 'short', day: 'numeric' })
    + ', ' + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

// ─────────────────────────────────────────────────────────────
// REALTIME SYNC (Without Reload flow)
// ─────────────────────────────────────────────────────────────
let _realtimeChannel = null;

function sbSubscribeToHomeworkChanges(onUpdateCallback) {
  if (!supabaseClient) return;
  if (_realtimeChannel) return; // already subscribed

  _realtimeChannel = supabaseClient.channel('custom-all-channel')
    .on(
      'postgres_changes',
      { event: '*', schema: 'public', table: 'homework' },
      async (payload) => {
        console.log('[MTS Realtime] Homework change detected!', payload);
        await loadAllFromSupabase();
        if (onUpdateCallback) onUpdateCallback();
      }
    )
    .on(
      'postgres_changes',
      { event: '*', schema: 'public', table: 'submissions' },
      async (payload) => {
        console.log('[MTS Realtime] Submission change detected!', payload);
        await loadAllFromSupabase();
        if (onUpdateCallback) onUpdateCallback();
      }
    )
    .subscribe();
}

console.log('[MTS] supabase-db.js loaded ✅');
