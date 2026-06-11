import re

def fix_nav_login():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    old_js = """if (screenId.includes('-chat')) {
          roleNav.style.display = 'none';
        } else {
          roleNav.style.display = 'flex';
        }"""
        
    new_js = """if (screenId.includes('-chat') || screenId === 'login') {
          roleNav.style.display = 'none';
        } else {
          roleNav.style.display = '';
        }"""
        
    if old_js in html:
        html = html.replace(old_js, new_js)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Login nav visibility fixed!")
    else:
        print("Could not find the exact JS block. Trying regex...")
        html = re.sub(r"if\s*\(\s*screenId\.includes\('-chat'\)\s*\)\s*\{\s*roleNav\.style\.display\s*=\s*'none';\s*\}\s*else\s*\{\s*roleNav\.style\.display\s*=\s*'flex';\s*\}", new_js, html)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Regex applied.")

if __name__ == '__main__':
    fix_nav_login()
