import re

def apply_dark_theme():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 1. Update CSS Variables for Dark Mode
    # I'll replace the existing :root { ... } with a dark mode version
    # Since there are multiple :root declarations possibly (from previous scripts), 
    # I'll just inject an override block at the end of the <style> that sets the dark theme.
    
    dark_css = """
    /* Premium Dark Theme Override */
    :root {
      --bg: #0F172A !important;
      --surface: rgba(30, 41, 59, 0.6) !important;
      --surface-solid: #1E293B !important;
      --text: #F8FAFC !important;
      --text-muted: #94A3B8 !important;
      --border: rgba(255, 255, 255, 0.1) !important;
      --shadow-glass: 0 8px 32px 0 rgba(0, 0, 0, 0.4) !important;
      --shadow-sm: 0 4px 6px rgba(0,0,0,0.3) !important;
    }
    
    body { background-color: #05080F !important; background-image: radial-gradient(circle at 50% 0%, #1E1B4B 0%, #05080F 80%) !important; }
    
    .screen-deck, .screen { background-color: var(--bg) !important; background-image: radial-gradient(circle at 50% 0%, #1E1B4B 0%, var(--bg) 80%) !important; color: var(--text) !important; }
    
    .card, .glass-card, .kpi-glass, .kpi-card {
      background: var(--surface) !important;
      backdrop-filter: blur(12px) !important;
      -webkit-backdrop-filter: blur(12px) !important;
      border: 1px solid var(--border) !important;
      color: var(--text) !important;
      box-shadow: var(--shadow-glass) !important;
    }
    
    .app-header {
      background: rgba(15, 23, 42, 0.7) !important;
      border-bottom: 1px solid var(--border) !important;
    }
    .app-header h1 { color: var(--text) !important; }
    .header-btn {
      background: var(--surface-solid) !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
    }
    .header-btn:active { background: #334155 !important; }
    
    .bottom-nav {
      background: rgba(15, 23, 42, 0.85) !important;
      border: 1px solid var(--border) !important;
    }
    .nav-item { color: var(--text-muted) !important; }
    .nav-item.active { color: var(--accent) !important; }
    .nav-item.active::after { background: var(--accent) !important; }
    
    .login-role-card {
      background: var(--surface) !important;
      backdrop-filter: blur(8px) !important;
      border: 1px solid var(--border) !important;
      color: var(--text) !important;
    }
    .login-role-card:hover { border-color: var(--accent) !important; background: rgba(30, 41, 59, 0.9) !important; }
    .role-title { color: var(--text) !important; }
    .role-desc { color: var(--text-muted) !important; }
    
    .smart-login-header h2 { color: var(--text) !important; }
    
    .status-bar { color: var(--text) !important; }
    .home-indicator-bar { background-color: #64748B !important; }
    
    .form-input { 
      background: var(--surface-solid) !important; 
      color: var(--text) !important; 
      border: 1px solid var(--border) !important;
    }
    .form-input::placeholder { color: var(--text-muted) !important; }
    
    .calendar-day {
      background: var(--surface) !important;
      border: 1px solid var(--border) !important;
      color: var(--text) !important;
    }
    .calendar-day.empty { background: transparent !important; border: none !important; }
    
    .segment-bar {
      background: var(--surface) !important;
      border: 1px solid var(--border) !important;
    }
    .segment-btn { color: var(--text-muted) !important; }
    .segment-btn.active {
      background: var(--primary) !important;
      color: white !important;
    }
    
    /* Global text overrides for inline styles */
    h1, h2, h3, h4, h5, h6 { color: var(--text) !important; }
    p { color: var(--text-muted) !important; }
    .text-gradient { 
      background: linear-gradient(135deg, #818CF8 0%, #22D3EE 100%) !important; 
      -webkit-background-clip: text !important; 
      -webkit-text-fill-color: transparent !important; 
    }
    
    /* Make the login spinner dark mode compatible */
    .loading-overlay { background: rgba(15, 23, 42, 0.8) !important; }
    .loading-overlay p { color: var(--text) !important; }
    
    /* Secondary and Danger buttons */
    .btn-secondary { background: var(--surface-solid) !important; color: var(--text) !important; }
    """
    
    if "Premium Dark Theme Override" not in html:
        html = html.replace('</style>', dark_css + '\n</style>')

    # 2. Fix inline style overrides that might clash
    # Some elements had hardcoded colors like color:#0F172A; or color:#64748B;
    html = html.replace('color: #0F172A;', 'color: var(--text);')
    html = html.replace('color: #64748B;', 'color: var(--text-muted);')
    html = html.replace('color:#0F172A;', 'color: var(--text);')
    html = html.replace('color:#64748B;', 'color: var(--text-muted);')
    
    # Let's ensure the user avatar circles have good contrast
    html = html.replace('color:var(--primary);', 'color:var(--text);')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Dark theme applied!")

if __name__ == '__main__':
    apply_dark_theme()
