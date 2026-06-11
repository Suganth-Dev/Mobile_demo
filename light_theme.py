import re

def apply_light_theme():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Strip the previous "Mixed Premium Theme Override"
    mixed_block = re.search(r'/\*\s*Mixed Premium Theme Override\s*\*/.*?(?=\*/|</style>)', html, re.DOTALL)
    if mixed_block:
        html = html.replace(mixed_block.group(0), '')
        html = html.replace('/* Mixed Premium Theme Override */', '')

    premium_light_css = """
    /* Unique Premium Light Theme Override */
    :root {
      --app-bg: #EEF2FF; /* Soft premium indigo-tinted light background */
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
    
    /* Fix the white bands on top and bottom of the phone */
    .smartphone {
      background: var(--app-bg-gradient) !important;
    }
    
    body { background-color: #0F172A !important; background-image: radial-gradient(circle at 50% 0%, #1E1B4B 0%, #0F172A 80%) !important; }
    
    .screen-deck, .screen { 
      background: transparent !important; 
      color: var(--text) !important; 
    }
    
    /* 2. Glass Cards & UI Elements */
    .card, .glass-card, .kpi-glass, .kpi-card {
      background: var(--surface-solid) !important;
      backdrop-filter: blur(20px) !important;
      -webkit-backdrop-filter: blur(20px) !important;
      border: 1px solid rgba(255,255,255,0.8) !important;
      color: var(--text) !important;
      box-shadow: var(--shadow-glass) !important;
      border-radius: 24px !important;
    }
    
    .app-header {
      background: rgba(238, 242, 255, 0.8) !important;
      backdrop-filter: blur(16px) !important;
      border-bottom: 1px solid var(--border) !important;
    }
    .app-header h1 { color: var(--text) !important; }
    
    .header-btn {
      background: #FFFFFF !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
      box-shadow: var(--shadow-sm) !important;
    }
    .header-btn:active { background: #EEF2FF !important; }
    
    .bottom-nav {
      background: rgba(255, 255, 255, 0.9) !important;
      backdrop-filter: blur(20px) !important;
      border: 1px solid var(--border) !important;
      box-shadow: 0 -4px 30px rgba(79, 70, 229, 0.08) !important;
    }
    .nav-item { color: var(--text-muted) !important; }
    .nav-item.active { color: var(--primary) !important; }
    .nav-item.active::after { background: var(--primary) !important; }
    
    .login-role-card {
      background: var(--surface-solid) !important;
      border: 1px solid var(--border) !important;
      color: var(--text) !important;
      box-shadow: var(--shadow-sm) !important;
      border-radius: 20px !important;
      transition: all 0.3s ease !important;
    }
    .login-role-card:hover { border-color: var(--primary) !important; transform: translateY(-3px); box-shadow: var(--shadow-glass) !important; }
    .role-title { color: var(--text) !important; font-weight: 800 !important; }
    .role-desc { color: var(--text-muted) !important; }
    
    .smart-login-header h2 { color: var(--text) !important; }
    .smart-login-header p { color: var(--text-muted) !important; }
    
    /* Fix Status bar and home indicator for light theme */
    .status-bar { color: #0F172A !important; } 
    .home-indicator-bar { background-color: #0F172A !important; }
    
    .form-input { 
      background: #FFFFFF !important; 
      color: var(--text) !important; 
      border: 1px solid rgba(99, 102, 241, 0.2) !important;
    }
    .form-input::placeholder { color: var(--text-muted) !important; }
    
    .calendar-day {
      background: var(--surface-solid) !important;
      border: 1px solid var(--border) !important;
      color: var(--text) !important;
    }
    .calendar-day.empty { background: transparent !important; border: none !important; box-shadow: none !important; }
    
    .segment-bar {
      background: rgba(255, 255, 255, 0.6) !important;
      border: 1px solid var(--border) !important;
      padding: 6px !important;
      border-radius: 16px !important;
    }
    .segment-btn { color: var(--text-muted) !important; }
    .segment-btn.active {
      background: #FFFFFF !important;
      color: var(--primary) !important;
      box-shadow: var(--shadow-sm) !important;
    }
    
    /* Global text overrides */
    h1, h2, h3, h4, h5, h6 { color: var(--text) !important; }
    p { color: var(--text-muted) !important; }
    
    .desktop-title, .desktop-title span { color: #FFFFFF !important; }
    
    .loading-overlay { background: rgba(238, 242, 255, 0.85) !important; }
    .loading-overlay p { color: var(--primary) !important; }
    
    .btn-secondary { background: #FFFFFF !important; color: var(--text) !important; border: 1px solid var(--border) !important; }
    """
    
    html = re.sub(r'</style>\s*</head>', '</style></head>', html)
    html = html.replace('</style></head>', premium_light_css + '\n</style>\n</head>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Premium light theme and smartphone bezel fix applied!")

if __name__ == '__main__':
    apply_light_theme()
