import re

def fix():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading: {e}")
        return

    # 1. Add status bar CSS and keyframes spin
    css_to_add = """
    /* Status Bar & Phone Elements */
    .status-bar {
      height: 44px;
      background-color: transparent;
      color: var(--text);
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 24px;
      font-size: 14px;
      font-weight: 600;
      z-index: 100;
      position: relative;
      margin-top: 6px;
    }
    .status-bar .notch {
      width: 140px;
      height: 30px;
      background-color: #1E293B;
      position: absolute;
      top: -6px;
      left: 50%;
      transform: translateX(-50%);
      border-bottom-left-radius: 20px;
      border-bottom-right-radius: 20px;
      z-index: 99;
    }
    .status-bar .left-indicators {
      display: flex; align-items: center; gap: 4px; z-index: 101; margin-top: -6px; font-family: -apple-system, BlinkMacSystemFont, sans-serif; letter-spacing: -0.2px; font-size: 15px;
    }
    .status-bar .right-indicators {
      display: flex; align-items: center; gap: 6px; z-index: 101; margin-top: -6px;
    }
    .home-indicator-bar {
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      width: 130px;
      height: 5px;
      background-color: #0F172A;
      border-radius: 100px;
      z-index: 100;
    }
    
    @keyframes spin { 100% { transform: rotate(360deg); } }
    .loading-overlay {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(255,255,255,0.7); backdrop-filter: blur(10px);
      z-index: 999; display: none; flex-direction: column; align-items: center; justify-content: center;
    }
    .spinner {
      width: 44px; height: 44px; border: 4px solid rgba(79, 70, 229, 0.2); border-top-color: var(--primary);
      border-radius: 50%; animation: spin 1s linear infinite;
    }
    """
    
    if ".status-bar {" not in html:
        html = html.replace('</style>', css_to_add + '\n</style>')

    # 2. Add login spinner to login screen
    login_spinner_html = """
          <div class="loading-overlay" id="login-spinner">
            <div class="spinner"></div>
            <p style="margin-top:16px;font-weight:700;font-family:var(--font-heading);color:var(--primary);">Authenticating...</p>
          </div>
    """
    
    # Insert right after <div class="screen" id="login">
    if 'id="login-spinner"' not in html:
        html = html.replace('<div class="screen" id="login">', '<div class="screen" id="login">' + login_spinner_html)
        
    # Also fix the login script to make sure it hides the spinner nicely
    # processLogin already does setTimeout 

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Fixed bugs!")

if __name__ == '__main__':
    fix()
