import re

def fix():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 1. Fix Bottom Nav visibility CSS
    # Current CSS: .bottom-nav { ... display: flex; ... }
    # We want to change 'display: flex;' inside .bottom-nav to 'display: none;'
    # and add .bottom-nav.active { display: flex; }
    
    # Let's find the exact .bottom-nav CSS definition
    nav_css_match = re.search(r'\.bottom-nav\s*\{[^}]*\}', html)
    if nav_css_match:
        nav_css = nav_css_match.group(0)
        new_nav_css = nav_css.replace('display: flex;', 'display: none;')
        new_nav_css += '\n    .bottom-nav.active { display: flex; }'
        html = html.replace(nav_css, new_nav_css)

    # 2. Fix the page reload issue in window.addEventListener("load")
    # Current logic:
    # setTimeout(() => {
    #   showScreen("login");
    # }, 2000);
    
    # We want to replace it with:
    # setTimeout(() => {
    #   if (DB && DB.currentUser) {
    #     renderBottomTabNav(DB.currentUser.role);
    #     showScreen(DB.currentUser.role + "-home");
    #   } else {
    #     showScreen("login");
    #   }
    # }, 2000);
    
    old_timeout = """setTimeout(() => {
        showScreen("login");
      }, 2000);"""
      
    new_timeout = """setTimeout(() => {
        if (DB && DB.currentUser && DB.currentUser.role) {
          renderBottomTabNav(DB.currentUser.role);
          showScreen(DB.currentUser.role + "-home");
        } else {
          showScreen("login");
        }
      }, 2000);"""
      
    html = html.replace(old_timeout, new_timeout)
    
    # If the exact indentation failed, try a regex replacement for the setTimeout block
    if old_timeout not in html:
        html = re.sub(
            r'setTimeout\(\(\)\s*=>\s*\{\s*showScreen\("login"\);\s*\},\s*2000\);',
            new_timeout,
            html
        )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Fixed logout nav bar and reload logic!")

if __name__ == '__main__':
    fix()
