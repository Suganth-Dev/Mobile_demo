import re
import sys

def rebuild():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 1. Replace the entire <style> block
    style_start = html.find('<style>')
    style_end = html.find('</style>')
    
    if style_start == -1 or style_end == -1:
        print("Could not find <style> tags")
        return

    new_css = """<style>
    /* ──────────────────────────────────────────────────────────────────
       1. SMART UI - MODERN GLASSMORPHISM DESIGN SYSTEM
       ────────────────────────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    :root {
      --primary: #4F46E5;       /* Modern Indigo */
      --primary-light: #818CF8;
      --accent: #06B6D4;        /* Cyan */
      --accent-light: #CFFAFE;
      --bg: #F8FAFC;            /* Very light slate */
      --surface: rgba(255, 255, 255, 0.85); /* Glassmorphic Surface */
      --surface-solid: #FFFFFF;
      --success: #10B981;
      --success-light: #D1FAE5;
      --warning: #F59E0B;
      --warning-light: #FEF3C7;
      --danger: #EF4444;
      --danger-light: #FEE2E2;
      --info: #3B82F6;
      --info-light: #DBEAFE;
      --text: #0F172A;
      --text-muted: #64748B;
      --border: rgba(226, 232, 240, 0.6);
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
      --shadow-glass: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
      
      --font-english: 'Inter', sans-serif;
      --font-tamil: 'Noto Sans Tamil', sans-serif;
      --font-heading: 'Plus Jakarta Sans', sans-serif;
      
      --transition-speed: 0.4s;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; user-select: none; }
    
    body {
      font-family: var(--font-english);
      background-color: #0F172A; /* Dark background for desktop wrapper */
      color: var(--text);
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      overflow: hidden;
      background-image: radial-gradient(circle at 50% 0%, #312E81 0%, #0F172A 70%);
    }

    body.lang-tamil .lang-en { display: none !important; }
    body:not(.lang-tamil) .lang-ta { display: none !important; }
    body.lang-tamil { font-family: var(--font-tamil), var(--font-english); }

    .desktop-container { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 24px; padding: 20px; z-index: 10; height: 100%; }
    
    .desktop-title { font-family: var(--font-heading); color: #F1F5F9; font-size: 24px; font-weight: 700; display: flex; align-items: center; gap: 12px; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }
    .desktop-title span { font-weight: 400; color: #94A3B8; font-size: 16px; }

    .phone-mockup {
      width: 390px; height: 844px;
      background-color: var(--bg);
      border: 12px solid #1E293B;
      border-radius: 50px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), inset 0 0 0 2px #334155;
      position: relative; overflow: hidden; display: flex; flex-direction: column;
    }
    
    /* Screen Deck & Layout */
    .screen-deck { flex: 1; position: relative; overflow: hidden; background-color: var(--bg); }
    .screen { position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; background-color: var(--bg); transform: translateX(100%); transition: transform var(--transition-speed) cubic-bezier(0.2, 0.8, 0.2, 1); opacity: 0; pointer-events: none; }
    .screen.active { transform: translateX(0); opacity: 1; pointer-events: auto; }
    
    .screen-content { flex: 1; overflow-y: auto; overflow-x: hidden; padding: 24px 20px 100px; }
    .screen-content::-webkit-scrollbar { display: none; }
    
    /* Smart UI Components */
    .glass-card {
      background: var(--surface);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 20px;
      box-shadow: var(--shadow-glass);
      margin-bottom: 16px;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .glass-card:active { transform: scale(0.98); }
    
    .card-title { font-family: var(--font-heading); font-size: 16px; font-weight: 700; color: var(--text); margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    
    .btn { border: none; border-radius: 14px; padding: 14px 20px; font-size: 15px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%; transition: all 0.2s; font-family: var(--font-heading); }
    .btn-primary { background: linear-gradient(135deg, var(--primary) 0%, #6366F1 100%); color: white; box-shadow: 0 4px 14px rgba(79, 70, 229, 0.3); }
    .btn-primary:active { transform: scale(0.96); box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3); }
    
    .form-group { margin-bottom: 20px; text-align: left; }
    .form-label { display: block; font-size: 13px; font-weight: 600; color: var(--text-muted); margin-bottom: 8px; font-family: var(--font-heading); }
    .form-input { width: 100%; padding: 14px 16px; border-radius: 12px; border: 1px solid var(--border); background-color: var(--surface-solid); color: var(--text); font-size: 15px; font-family: var(--font-english); outline: none; transition: border-color 0.2s, box-shadow 0.2s; }
    .form-input:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1); }
    
    /* Login Screen Specifics */
    .smart-login-header {
      text-align: center; margin-top: 20px; margin-bottom: 40px; animation: slideDown 0.6s ease-out;
    }
    @keyframes slideDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
    
    .login-role-card {
      background: var(--surface-solid);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 12px;
      cursor: pointer;
      transition: all 0.2s;
      box-shadow: var(--shadow-sm);
      animation: fadeIn 0.5s ease-out forwards;
      opacity: 0;
      transform: translateY(10px);
    }
    @keyframes fadeIn { to { opacity: 1; transform: translateY(0); } }
    .login-role-card:nth-child(1) { animation-delay: 0.1s; }
    .login-role-card:nth-child(2) { animation-delay: 0.2s; }
    .login-role-card:nth-child(3) { animation-delay: 0.3s; }
    
    .login-role-card:hover { border-color: var(--primary); box-shadow: var(--shadow); transform: translateY(-2px); }
    .login-role-card:active { transform: translateY(0) scale(0.98); }
    .role-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; background: var(--bg); }
    .role-info { text-align: left; flex: 1; }
    .role-title { font-family: var(--font-heading); font-weight: 700; font-size: 16px; color: var(--text); }
    .role-desc { font-size: 12px; color: var(--text-muted); margin-top: 2px; }
    
    /* App Header */
    .app-header { padding: 20px 20px 10px; background: var(--bg); display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 50; }
    .app-header h1 { font-family: var(--font-heading); font-size: 22px; font-weight: 800; color: var(--text); }
    
    /* Modern Bottom Nav */
    .bottom-nav { position: absolute; bottom: 30px; left: 20px; right: 20px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(16px); border-radius: 24px; display: flex; justify-content: space-around; padding: 12px 8px; box-shadow: var(--shadow-glass); border: 1px solid var(--border); z-index: 200; }
    .nav-item { display: flex; flex-direction: column; align-items: center; gap: 4px; color: var(--text-muted); cursor: pointer; transition: all 0.2s; position: relative; width: 60px; }
    .nav-item i { width: 22px; height: 22px; stroke-width: 2px; transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); }
    .nav-item span { font-size: 10px; font-weight: 600; font-family: var(--font-heading); }
    .nav-item.active { color: var(--primary); }
    .nav-item.active i { transform: translateY(-4px); stroke-width: 2.5px; }
    .nav-item.active::after { content: ''; position: absolute; bottom: -8px; width: 4px; height: 4px; background: var(--primary); border-radius: 50%; }

    /* KPI Grid Glass */
    .kpi-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 16px; }
    .kpi-glass { background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.5) 100%); backdrop-filter: blur(10px); border: 1px solid white; border-radius: 16px; padding: 16px; text-align: center; box-shadow: var(--shadow-sm); }
    .kpi-num { font-family: var(--font-heading); font-size: 28px; font-weight: 800; color: var(--primary); margin-bottom: 4px; }
    .kpi-label { font-size: 12px; color: var(--text-muted); font-weight: 600; }

    /* Badge */
    .badge { padding: 4px 10px; border-radius: 99px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
    .badge-success { background: var(--success-light); color: var(--success); }
    .badge-info { background: var(--info-light); color: var(--info); }
    .badge-primary { background: rgba(79, 70, 229, 0.1); color: var(--primary); }

    /* List Items */
    .list-item { display: flex; align-items: center; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--border); }
    .list-item:last-child { border-bottom: none; }
    
    /* Utilities */
    .text-gradient { background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    /* Hide scrollbars globally */
    ::-webkit-scrollbar { display: none; }
    </style>"""

    html = html[:style_start] + new_css + html[style_end + 8:]

    # 2. Replace Login Screen HTML
    login_start = html.find('<div class="screen" id="login">')
    login_end = html.find('<!-- ════ SCREEN 3: PARENT HOME SCREEN ════ -->')
    if login_start != -1 and login_end != -1:
        new_login = """<div class="screen" id="login">
          <div class="screen-content" style="padding: 24px; display: flex; flex-direction: column; justify-content: center; height: 100%;">
            <div class="smart-login-header">
              <div style="width: 80px; height: 80px; background: var(--surface-solid); border: 1.5px solid var(--border); border-radius: 24px; display: inline-flex; align-items: center; justify-content: center; box-shadow: var(--shadow-glass); margin-bottom: 20px; transform: rotate(-5deg); padding: 8px; box-sizing: border-box;">
                <img class="logo-light" src="logo-blue.png?v=7" alt="MTS Logo" style="width: 100%; height: 100%; object-fit: contain;">
                <img class="logo-dark" src="logo-silver.png?v=7" alt="MTS Logo" style="width: 100%; height: 100%; object-fit: contain;">
              </div>
              <h2 style="font-family: var(--font-heading); font-weight: 800; font-size: 28px; color: var(--text);">Welcome to <br><span class="text-gradient">MTS Connect</span></h2>
              <p style="font-size: 14px; color: var(--text-muted); margin-top: 8px;" class="lang-en">Select your role to explore the smart campus.</p>
              <p style="font-size: 14px; color: var(--text-muted); margin-top: 8px;" class="lang-ta">ஸ்மார்ட் வளாகத்தை ஆராய உங்கள் பாத்திரத்தைத் தேர்ந்தெடுக்கவும்.</p>
            </div>
            
            <div class="demo-login-cards" style="margin-top: 20px;">
              <div class="login-role-card" onclick="fillCreds('parent'); processLogin();">
                <div class="role-icon" style="background: rgba(16, 185, 129, 0.1); color: #10B981;">👨‍👩‍👦</div>
                <div class="role-info">
                  <div class="role-title">Parent Portal</div>
                  <div class="role-desc">View attendance, homework & news</div>
                </div>
                <i data-lucide="chevron-right" style="color: #CBD5E1;"></i>
              </div>
              
              <div class="login-role-card" onclick="fillCreds('teacher'); processLogin();">
                <div class="role-icon" style="background: rgba(59, 130, 246, 0.1); color: #3B82F6;">👩‍🏫</div>
                <div class="role-info">
                  <div class="role-title">Teacher Dashboard</div>
                  <div class="role-desc">Manage classes & grading</div>
                </div>
                <i data-lucide="chevron-right" style="color: #CBD5E1;"></i>
              </div>

              <div class="login-role-card" onclick="fillCreds('admin'); processLogin();">
                <div class="role-icon" style="background: rgba(245, 158, 11, 0.1); color: #F59E0B;">👑</div>
                <div class="role-info">
                  <div class="role-title">Admin Console</div>
                  <div class="role-desc">School oversight & approvals</div>
                </div>
                <i data-lucide="chevron-right" style="color: #CBD5E1;"></i>
              </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
              <button onclick="toggleLanguage()" style="background: none; border: none; color: var(--primary); font-size: 13px; font-weight: 600; cursor: pointer; display: inline-flex; align-items: center; gap: 4px;">
                <i data-lucide="languages" style="width: 16px; height: 16px;"></i> Change Language
              </button>
            </div>
          </div>
        </div>
        
        <!-- Hidden traditional form to keep JS logic intact -->
        <form id="login-form" style="display:none;">
            <input type="email" id="login-email">
            <input type="password" id="login-password">
        </form>

        """
        html = html[:login_start] + new_login + html[login_end:]

    # 3. Replace Parent Home Screen to use Glass Cards
    phome_start = html.find('<div class="screen" id="parent-home">')
    phome_end = html.find('<!-- ════ SCREEN 4: PARENT CHILDREN LIST ════ -->')
    
    if phome_start != -1 and phome_end != -1:
        new_phome = """<div class="screen" id="parent-home">
          <div class="app-header">
            <div>
              <h1 class="lang-en" style="font-size: 24px;">Parent <span class="text-gradient">Portal</span></h1>
              <h1 class="lang-ta" style="font-size: 24px;">பெற்றோர் <span class="text-gradient">தளம்</span></h1>
            </div>
            <button style="border: none; background: var(--surface); box-shadow: var(--shadow-sm); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--text);" onclick="toggleLanguage()"><i data-lucide="bell"></i></button>
          </div>
          
          <div class="screen-content" style="padding-top: 10px;">
            <!-- Modern Student Switcher -->
            <div class="glass-card" style="padding: 12px; display: flex; gap: 8px; overflow-x: auto; margin-bottom: 24px;" id="parent-child-toggle">
               <!-- Will be populated by JS, but let's restyle it via CSS. We rely on the existing JS logic. -->
               <div class="child-pill active" onclick="switchChild('Anika Kumar')" style="padding: 8px 16px; background: var(--primary); color: white; border-radius: 12px; font-weight: 600; font-size: 13px;">Anika Kumar</div>
               <div class="child-pill" onclick="switchChild('Rohan Kumar')" style="padding: 8px 16px; background: transparent; color: var(--text-muted); border-radius: 12px; font-weight: 600; font-size: 13px;">Rohan Kumar</div>
            </div>

            <!-- Smart Hero Widget -->
            <div class="glass-card" style="background: linear-gradient(135deg, var(--primary) 0%, #312E81 100%); color: white; border: none; box-shadow: 0 10px 25px rgba(79, 70, 229, 0.4); position: relative; overflow: hidden;">
              <div style="position: absolute; top: -20px; right: -20px; width: 100px; height: 100px; background: rgba(255,255,255,0.1); border-radius: 50%; blur: 20px;"></div>
              <span class="badge" style="background: rgba(255,255,255,0.2); color: white; margin-bottom: 12px; display: inline-block;">Word of the Day</span>
              <h2 style="font-size: 28px; font-weight: 800; font-family: var(--font-tamil); margin-bottom: 4px;">வணக்கம்</h2>
              <p style="font-size: 14px; opacity: 0.9;" class="lang-en">Vanakkam • Hello / Welcome</p>
            </div>

            <!-- KPI Grid -->
            <div class="kpi-grid">
              <div class="kpi-glass" onclick="showScreen('parent-attendance')">
                <div class="kpi-num" id="parent-kpi-att">90%</div>
                <div class="kpi-label lang-en">Attendance</div>
                <div class="kpi-label lang-ta">வருகைப்பதிவு</div>
              </div>
              <div class="kpi-glass" onclick="showScreen('parent-homework')">
                <div class="kpi-num" id="parent-kpi-hw">1/2</div>
                <div class="kpi-label lang-en">Homework</div>
                <div class="kpi-label lang-ta">வீட்டுப்பாடம்</div>
              </div>
            </div>

            <!-- Announcements -->
            <div class="glass-card">
              <div class="card-title">
                <span class="lang-en">Latest Updates</span>
                <button style="border:none; background:none; color:var(--primary); font-size:13px; font-weight:600;" onclick="showScreen('parent-announcements')">View All</button>
              </div>
              <div id="parent-home-announcements-list" style="display: flex; flex-direction: column; gap: 12px;">
                <!-- JS will populate this -->
                <div style="display: flex; gap: 12px; align-items: center; padding: 8px 0; border-bottom: 1px solid var(--border);">
                  <div style="width: 40px; height: 40px; border-radius: 10px; background: var(--accent-light); color: var(--accent); display: flex; align-items: center; justify-content: center;"><i data-lucide="megaphone"></i></div>
                  <div style="flex: 1;">
                    <h4 style="font-size: 14px; font-weight: 600; color: var(--text);">School Annual Day</h4>
                    <p style="font-size: 12px; color: var(--text-muted);">Join us next Saturday</p>
                  </div>
                </div>
              </div>
            </div>
            
            <div style="height: 60px;"></div> <!-- Spacer for bottom nav -->
          </div>
        </div>
        
        """
        html = html[:phome_start] + new_phome + html[phome_end:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Successfully overhauled UI!")

if __name__ == '__main__':
    rebuild()
