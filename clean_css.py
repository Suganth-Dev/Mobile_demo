import re

def clean_css():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Find the start of the first injected block
    start_marker = "/* Status Bar & Phone Elements */"
    start_idx = html.find(start_marker)
    
    if start_idx == -1:
        print("Could not find the start marker.")
        # Maybe it's missing, let's search for "/* Restored Global Utility Classes"
        start_marker = "/* Restored Global Utility Classes"
        start_idx = html.find(start_marker)
        
    if start_idx == -1:
        print("Could not find any injected block marker. Searching for </style>")
        # We will just append if we can't find it, but we MUST clean up the stray */
        html = re.sub(r'\*/\s*h1, h2, h3', 'h1, h2, h3', html)
        html = re.sub(r'\*/\s*--bg-dark', '--bg-dark', html)
        pass # Better to just replace the whole thing
    else:
        # Delete everything from start_idx to the last </style>
        end_idx = html.rfind("</style>")
        if end_idx != -1:
            clean_html = html[:start_idx]
            clean_html += "\n"
            
            # Now we inject the consolidated clean CSS
            consolidated_css = """
    /* --- COMBINED PREMIUM LIGHT THEME & UTILITIES --- */
    
    :root {
      --app-bg: #EEF2FF; 
      --app-bg-gradient: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%);
      --surface: rgba(255, 255, 255, 0.85) !important;
      --surface-solid: #FFFFFF !important;
      --text: #0F172A !important;
      --text-muted: #64748B !important;
      --border: rgba(99, 102, 241, 0.1) !important;
      --shadow-glass: 0 10px 40px rgba(79, 70, 229, 0.08) !important;
      --shadow-sm: 0 4px 10px rgba(79, 70, 229, 0.05) !important;
      --primary: #4F46E5 !important;
    }
    
    body { background-color: #0F172A !important; background-image: radial-gradient(circle at 50% 0%, #1E1B4B 0%, #0F172A 80%) !important; }
    
    .smartphone { background: var(--app-bg-gradient) !important; }
    
    .screen-deck, .screen { background: transparent !important; color: var(--text) !important; }
    
    /* Global Utility Classes */
    .card, .glass-card, .kpi-glass, .kpi-card {
      background: var(--surface-solid) !important;
      backdrop-filter: blur(20px) !important;
      -webkit-backdrop-filter: blur(20px) !important;
      border: 1px solid rgba(255,255,255,0.8) !important;
      color: var(--text) !important;
      box-shadow: var(--shadow-glass) !important;
      border-radius: 24px !important;
      padding: 24px;
      margin-bottom: 16px;
    }
    
    .app-header { 
      padding: 12px 20px; 
      background: rgba(238, 242, 255, 0.8) !important; 
      backdrop-filter: blur(16px) !important;
      -webkit-backdrop-filter: blur(16px) !important;
      display: grid !important; 
      grid-template-columns: 40px 1fr 40px; 
      align-items: center; 
      position: sticky; top: 0; z-index: 50; 
      border-bottom: 1px solid var(--border) !important;
    }
    .app-header h1 { grid-column: 2; text-align: center; font-size: 18px !important; font-weight: 700; color: var(--text) !important; margin: 0; }
    
    .header-btn { 
      background: #FFFFFF !important; border: 1px solid var(--border) !important; width: 40px; height: 40px; border-radius: 50%; 
      display: flex; align-items: center; justify-content: center; color: var(--text) !important; cursor: pointer; 
      box-shadow: var(--shadow-sm) !important; transition: all 0.2s ease;
    }
    .header-btn:active { transform: scale(0.95); background: #EEF2FF !important; }
    
    .app-header .header-btn[onclick*="backward"] { grid-column: 1; justify-self: start; }
    .app-header .header-btn[onclick*="toggleLanguage"], .app-header .header-btn[onclick*="bell"] { grid-column: 3; justify-self: end; }
    
    .bottom-nav {
      background: rgba(255, 255, 255, 0.9) !important; backdrop-filter: blur(20px) !important; border: 1px solid var(--border) !important;
      box-shadow: 0 -4px 30px rgba(79, 70, 229, 0.08) !important; position: absolute; bottom: 30px; left: 20px; right: 20px; 
      border-radius: 24px; display: none; justify-content: space-around; padding: 12px 8px; z-index: 200;
    }
    .bottom-nav.active { display: flex; }
    .nav-item { display: flex; flex-direction: column; align-items: center; gap: 4px; color: var(--text-muted) !important; cursor: pointer; transition: all 0.2s; position: relative; width: 60px; }
    .nav-item.active { color: var(--primary) !important; }
    .nav-item.active::after { content: ''; width: 6px; height: 6px; background-color: var(--primary) !important; border-radius: 50%; position: absolute; bottom: -10px; }
    
    .login-role-card { background: var(--surface-solid) !important; border: 1px solid var(--border) !important; color: var(--text) !important; box-shadow: var(--shadow-sm) !important; border-radius: 20px !important; padding: 16px; margin-bottom: 12px; display: flex; align-items: center; cursor: pointer; transition: all 0.3s ease !important; }
    .login-role-card:hover { border-color: var(--primary) !important; transform: translateY(-3px); box-shadow: var(--shadow-glass) !important; }
    
    .status-bar { height: 44px; color: #0F172A !important; display: flex; justify-content: space-between; align-items: center; padding: 0 24px; font-size: 14px; font-weight: 600; z-index: 100; position: relative; margin-top: 6px; }
    .status-bar .notch { width: 140px; height: 30px; background-color: #1E293B; position: absolute; top: -6px; left: 50%; transform: translateX(-50%); border-bottom-left-radius: 20px; border-bottom-right-radius: 20px; z-index: 99; }
    .status-bar .left-indicators { display: flex; align-items: center; gap: 4px; z-index: 101; margin-top: -6px; font-family: -apple-system, BlinkMacSystemFont, sans-serif; letter-spacing: -0.2px; font-size: 15px; }
    .status-bar .right-indicators { display: flex; align-items: center; gap: 6px; z-index: 101; margin-top: -6px; }
    .home-indicator-bar { position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%); width: 130px; height: 5px; background-color: #0F172A !important; border-radius: 100px; z-index: 100; }
    
    @keyframes spin { 100% { transform: rotate(360deg); } }
    .loading-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(238, 242, 255, 0.85) !important; backdrop-filter: blur(10px); z-index: 999; display: none; flex-direction: column; align-items: center; justify-content: center; }
    .spinner { width: 44px; height: 44px; border: 4px solid rgba(79, 70, 229, 0.2); border-top-color: var(--primary); border-radius: 50%; animation: spin 1s linear infinite; }
    .loading-overlay p { color: var(--primary) !important; font-weight: 700; margin-top: 16px; font-family: var(--font-heading); }
    
    .form-input { background: #FFFFFF !important; color: var(--text) !important; border: 1px solid rgba(99, 102, 241, 0.2) !important; width: 100%; padding: 12px; border-radius: 12px; font-size: 14px; margin-bottom: 12px; }
    .form-input::placeholder { color: var(--text-muted) !important; }
    
    .btn-secondary { background: #FFFFFF !important; color: var(--text) !important; border: 1px solid var(--border) !important; }
    .btn-accent { background: var(--accent); color: white; border: none; padding: 12px; border-radius: 12px; font-weight: 600; cursor: pointer; }
    .btn-danger { background: var(--danger-light); color: var(--danger); border: 1px solid rgba(239, 68, 68, 0.2); }
    
    .badge-danger { background: var(--danger-light); color: var(--danger); }
    .badge-warning { background: var(--warning-light); color: var(--warning); }
    .badge-info { background: #DBEAFE; color: #1D4ED8; }
    .badge-muted { background: var(--surface-solid); color: var(--text-muted); border: 1px solid var(--border); }
    .badge-success { background: var(--success-light); color: var(--success); }
    .badge { padding: 4px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    
    .calendar-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; margin-top: 10px; }
    .calendar-day { background: var(--surface-solid) !important; border: 1px solid var(--border) !important; color: var(--text) !important; aspect-ratio: 1; border-radius: 10px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; position: relative; cursor: pointer; box-shadow: var(--shadow-sm); }
    .calendar-day.empty { background: transparent !important; border: none !important; box-shadow: none !important; }
    .calendar-day.event::after { content: ''; width: 4px; height: 4px; background-color: var(--accent); border-radius: 50%; position: absolute; bottom: 4px; }
    .calendar-day.holiday { background-color: var(--danger-light); color: var(--danger); border-color: rgba(239, 68, 68, 0.2); }
    
    .segment-bar { background: rgba(255, 255, 255, 0.6) !important; border: 1px solid var(--border) !important; padding: 6px !important; border-radius: 16px !important; display: flex; margin-bottom: 16px; backdrop-filter: blur(8px); }
    .segment-btn { color: var(--text-muted) !important; flex: 1; border: none; background: none; padding: 8px; font-size: 13px; font-weight: 600; border-radius: 10px; cursor: pointer; transition: all 0.2s; font-family: var(--font-heading); }
    .segment-btn.active { background: #FFFFFF !important; color: var(--primary) !important; box-shadow: var(--shadow-sm) !important; }
    
    .profile-avatar-circle { width: 80px; height: 80px; background: linear-gradient(135deg, var(--primary) 0%, #6366F1 100%); color: white; border-radius: 24px; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: 800; font-family: var(--font-heading); box-shadow: 0 10px 20px rgba(79, 70, 229, 0.3); margin: 0 auto 16px; }
    .account-header { text-align: center; margin-top: 20px; margin-bottom: 30px; }
    .account-name { font-size: 20px; font-weight: 700; color: var(--text) !important; font-family: var(--font-heading); }
    .account-email { font-size: 12px; color: var(--text-muted); margin-top: 4px; }
    
    h1, h2, h3, h4, h5, h6 { color: var(--text) !important; line-height: 1.3; }
    p { color: var(--text-muted) !important; line-height: 1.5; }
    .text-gradient { background: linear-gradient(135deg, #818CF8 0%, #22D3EE 100%) !important; -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; }
    .desktop-title, .desktop-title span { color: #FFFFFF !important; }
    
    .role-title { color: var(--text) !important; font-weight: 800 !important; }
    .role-desc { color: var(--text-muted) !important; }
    .smart-login-header h2 { color: var(--text) !important; }
    .smart-login-header p { color: var(--text-muted) !important; }
            """
            
            clean_html += consolidated_css + "\n</style>"
            clean_html += html[end_idx + 8:]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(clean_html)
            print("CSS perfectly cleaned and consolidated!")
            return
            
if __name__ == '__main__':
    clean_css()
