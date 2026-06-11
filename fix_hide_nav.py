import re

def fix_hide_nav():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Find where targetScreen.classList.add('active'); is in showScreen
    target_str = "targetScreen.classList.add('active');"
    
    inject_js = """targetScreen.classList.add('active');
      
      // Hide bottom nav on chat screens to prevent overlapping chat input
      const roleNav = document.getElementById('role-bottom-nav');
      if (roleNav) {
        if (screenId.includes('-chat')) {
          roleNav.style.display = 'none';
        } else {
          roleNav.style.display = 'flex';
        }
      }"""
      
    if "// Hide bottom nav on chat screens" not in html:
        html = html.replace(target_str, inject_js)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Injected JS to hide bottom nav on chat screens!")
    else:
        print("JS already injected.")

if __name__ == '__main__':
    fix_hide_nav()
