import re

def add_global_css():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    missing_css = """
    /* Restored Global Utility Classes for all 34 screens to look Glassmorphic */
    
    .card {
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
    .card:active { transform: scale(0.98); }
    
    .kpi-card {
      background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.5) 100%);
      backdrop-filter: blur(10px);
      border: 1px solid white;
      border-radius: 16px;
      padding: 16px;
      text-align: center;
      box-shadow: var(--shadow-sm);
    }
    
    .btn-secondary { background: transparent; color: var(--text); border: 1px solid var(--border); }
    .btn-accent { background: var(--accent); color: white; }
    .btn-danger { background: var(--danger-light); color: var(--danger); border: 1px solid rgba(239, 68, 68, 0.2); }
    
    .badge-danger { background: var(--danger-light); color: var(--danger); }
    .badge-warning { background: var(--warning-light); color: var(--warning); }
    .badge-muted { background: var(--bg); color: var(--text-muted); border: 1px solid var(--border); }
    
    .segment-bar {
      display: flex;
      background-color: rgba(255,255,255,0.5);
      padding: 4px;
      border-radius: 14px;
      margin-bottom: 16px;
      border: 1px solid var(--border);
      backdrop-filter: blur(8px);
    }
    .segment-btn {
      flex: 1;
      border: none;
      background: none;
      padding: 8px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      border-radius: 10px;
      cursor: pointer;
      transition: all 0.2s;
      font-family: var(--font-heading);
    }
    .segment-btn.active {
      background-color: var(--surface-solid);
      color: var(--primary);
      box-shadow: var(--shadow-sm);
    }
    
    /* Calendar */
    .calendar-grid {
      display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; margin-top: 10px;
    }
    .calendar-day {
      aspect-ratio: 1;
      background: rgba(255,255,255,0.6);
      border-radius: 10px;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      font-size: 13px; font-weight: 600; position: relative; cursor: pointer;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
    }
    .calendar-day.empty { background: transparent; box-shadow: none; border: none; }
    .calendar-day.event::after {
      content: ''; width: 4px; height: 4px; background-color: var(--accent); border-radius: 50%; position: absolute; bottom: 4px;
    }
    .calendar-day.holiday { background-color: var(--danger-light); color: var(--danger); border-color: rgba(239, 68, 68, 0.2); }
    
    /* Profile Avatar Circle */
    .profile-avatar-circle {
      width: 80px; height: 80px;
      background: linear-gradient(135deg, var(--primary) 0%, #6366F1 100%);
      color: white; border-radius: 24px;
      display: flex; align-items: center; justify-content: center;
      font-size: 28px; font-weight: 800; font-family: var(--font-heading);
      box-shadow: 0 10px 20px rgba(79, 70, 229, 0.3);
      margin: 0 auto 16px;
    }
    
    /* Account Page Headers */
    .account-header { text-align: center; margin-top: 20px; margin-bottom: 30px; }
    .account-name { font-size: 20px; font-weight: 700; color: var(--primary); font-family: var(--font-heading); }
    .account-email { font-size: 12px; color: var(--text-muted); margin-top: 4px; }
    """

    # Inject missing CSS right before </style>
    if "Restored Global Utility Classes" not in html:
        html = html.replace('</style>', missing_css + '\n</style>')

    # Fix the Account pages HTML to use the new avatar circle since they might have inline styles
    html = re.sub(r'<div style="width:64px;height:64px;background-color:var\(--primary\);color:var\(--surface\);border-radius:50%;font-size:24px;font-weight:700;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;">(.*?)</div>', 
                  r'<div class="profile-avatar-circle">\1</div>', html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Injected global utility CSS successfully!")

if __name__ == '__main__':
    add_global_css()
