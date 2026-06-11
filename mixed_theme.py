import re

def apply_mixed_theme():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # First, let's strip the previous "Premium Dark Theme Override" block so it doesn't conflict
    dark_block_match = re.search(r'/\*\s*Premium Dark Theme Override\s*\*/.*?(?=\*/|</style>)', html, re.DOTALL)
    if dark_block_match:
        html = html.replace(dark_block_match.group(0), '')
        # Clean up any trailing '*/' or similar if left over
        html = html.replace('/* Premium Dark Theme Override */', '')
        
    # We also might have left `</style>` tags or messy injections. Let's make sure we just append the new theme.
    mixed_css = """
    /* Mixed Premium Theme Override */
    :root {
      /* Keep the original light surfaces, but use dark for the background */
      --bg-dark: #0F172A;
      --surface: rgba(255, 255, 255, 0.95) !important;
      --surface-solid: #FFFFFF !important;
      --text: #0F172A !important;
      --text-muted: #64748B !important;
      --border: rgba(0, 0, 0, 0.05) !important;
      --shadow-glass: 0 10px 40px rgba(0, 0, 0, 0.15) !important;
      --shadow-sm: 0 4px 6px rgba(0,0,0,0.05) !important;
    }
    
    /* 1. Dark Backgrounds */
    body { background-color: #05080F !important; background-image: radial-gradient(circle at 50% 0%, #1E1B4B 0%, #05080F 80%) !important; }
    .screen-deck, .screen { 
      background-color: var(--bg-dark) !important; 
      background-image: radial-gradient(circle at 50% 0%, #1E1B4B 0%, var(--bg-dark) 80%) !important; 
      color: var(--text) !important; 
    }
    
    /* 2. White Glass Cards & UI Elements */
    .card, .glass-card, .kpi-glass, .kpi-card {
      background: var(--surface) !important;
      backdrop-filter: blur(12px) !important;
      -webkit-backdrop-filter: blur(12px) !important;
      border: 1px solid rgba(255,255,255,0.5) !important;
      color: var(--text) !important;
      box-shadow: var(--shadow-glass) !important;
      border-radius: 24px !important;
    }
    
    .app-header {
      background: rgba(255, 255, 255, 0.9) !important;
      backdrop-filter: blur(16px) !important;
      border-bottom: 1px solid var(--border) !important;
    }
    .app-header h1 { color: var(--text) !important; }
    
    .header-btn {
      background: #F8FAFC !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
    }
    .header-btn:active { background: #E2E8F0 !important; }
    
    .bottom-nav {
      background: rgba(255, 255, 255, 0.95) !important;
      border: 1px solid var(--border) !important;
      box-shadow: 0 -4px 20px rgba(0,0,0,0.1) !important;
    }
    .nav-item { color: var(--text-muted) !important; }
    .nav-item.active { color: var(--primary) !important; }
    .nav-item.active::after { background: var(--primary) !important; }
    
    .login-role-card {
      background: var(--surface) !important;
      backdrop-filter: blur(12px) !important;
      border: 1px solid var(--border) !important;
      color: var(--text) !important;
      box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }
    .login-role-card:hover { border-color: var(--primary) !important; transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important; }
    .role-title { color: var(--text) !important; }
    .role-desc { color: var(--text-muted) !important; }
    
    .smart-login-header h2 { color: #FFFFFF !important; } /* Welcome text on dark bg should be white */
    .smart-login-header p { color: #CBD5E1 !important; }
    
    .status-bar { color: #FFFFFF !important; } /* Status bar text on dark bg should be white */
    .home-indicator-bar { background-color: #FFFFFF !important; }
    
    .form-input { 
      background: #F8FAFC !important; 
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
      background: rgba(241, 245, 249, 0.8) !important;
      border: 1px solid var(--border) !important;
    }
    .segment-btn { color: var(--text-muted) !important; }
    .segment-btn.active {
      background: #FFFFFF !important;
      color: var(--text) !important;
      box-shadow: var(--shadow-sm) !important;
    }
    
    /* Global text overrides to ensure white cards have dark text */
    h1, h2, h3, h4, h5, h6 { color: var(--text) !important; }
    p { color: var(--text-muted) !important; }
    
    /* Exception: any header text or paragraphs outside of cards (like app title) */
    .desktop-title, .desktop-title span { color: #FFFFFF !important; }
    
    .loading-overlay { background: rgba(255, 255, 255, 0.85) !important; }
    .loading-overlay p { color: var(--text) !important; }
    
    .btn-secondary { background: transparent !important; color: var(--text) !important; border: 1px solid var(--border) !important; }
    """
    
    # Let's cleanly inject it
    # We will remove any trailing `</style>` that we might have messed up and place it cleanly.
    html = re.sub(r'</style>\s*</head>', '</style></head>', html)
    html = html.replace('</style></head>', mixed_css + '\n</style>\n</head>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Mixed theme applied!")

if __name__ == '__main__':
    apply_mixed_theme()
