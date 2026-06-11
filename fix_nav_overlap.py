import re

def fix_nav_overlap():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # We want to modify the showScreen function to hide bottom navs on chat screens
    # Let's find the showScreen function body
    
    # Let's look for the exact JS lines where it activates the bottom nav
    old_parent_logic = "if (screenId.startsWith('parent-')) {\n        document.getElementById('parent-bottom-nav').classList.add('active');"
    new_parent_logic = "if (screenId.startsWith('parent-') && !screenId.includes('chat')) {\n        document.getElementById('parent-bottom-nav').classList.add('active');"
    
    old_teacher_logic = "else if (screenId.startsWith('teacher-')) {\n        document.getElementById('teacher-bottom-nav').classList.add('active');"
    new_teacher_logic = "else if (screenId.startsWith('teacher-') && !screenId.includes('chat')) {\n        document.getElementById('teacher-bottom-nav').classList.add('active');"
    
    old_admin_logic = "else if (screenId.startsWith('admin-')) {\n        document.getElementById('admin-bottom-nav').classList.add('active');"
    new_admin_logic = "else if (screenId.startsWith('admin-') && !screenId.includes('chat')) {\n        document.getElementById('admin-bottom-nav').classList.add('active');"

    if old_parent_logic in html:
        html = html.replace(old_parent_logic, new_parent_logic)
        html = html.replace(old_teacher_logic, new_teacher_logic)
        html = html.replace(old_admin_logic, new_admin_logic)
        
        # We also need to fix the padding on the chat screen to ensure the chat input is exactly at the bottom of the phone.
        # Currently, .chat-input-bar has padding-bottom: 24px; which is good for the home indicator.
        # But we need to make sure the chat-box has enough padding-bottom so the last message isn't hidden by the input bar.
        
        html = html.replace('.chat-box { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; padding: 20px; padding-bottom: 100px; height: 100%; }', 
                            '.chat-box { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; padding: 20px; padding-bottom: 120px; height: 100%; }')

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Bottom nav hidden on chat screens successfully!")
    else:
        # Maybe it's already modified or slightly different spacing.
        # Let's use regex to be safe.
        html = re.sub(r"if\s*\(\s*screenId\.startsWith\('parent-'\)\s*\)\s*\{", "if (screenId.startsWith('parent-') && !screenId.includes('chat')) {", html)
        html = re.sub(r"else if\s*\(\s*screenId\.startsWith\('teacher-'\)\s*\)\s*\{", "else if (screenId.startsWith('teacher-') && !screenId.includes('chat')) {", html)
        html = re.sub(r"else if\s*\(\s*screenId\.startsWith\('admin-'\)\s*\)\s*\{", "else if (screenId.startsWith('admin-') && !screenId.includes('chat')) {", html)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Regex replaced bottom nav logic!")

if __name__ == '__main__':
    fix_nav_overlap()
