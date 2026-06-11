import re

def fix_design():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 1. Fix bottom nav items
    html = html.replace('class="nav-tab active"', 'class="nav-item active"')
    html = html.replace('class="nav-tab"', 'class="nav-item"')
    html = html.replace('.querySelectorAll(".nav-tab")', '.querySelectorAll(".nav-item")')
    
    # 2. Fix the bottom nav container class
    html = re.sub(r'id="role-bottom-nav"(\s*)class="[^"]*"', r'id="role-bottom-nav"\1class="bottom-nav"', html)
    # If it doesn't have a class attribute:
    if 'id="role-bottom-nav" class="bottom-nav"' not in html and 'class="bottom-nav" id="role-bottom-nav"' not in html:
        html = html.replace('id="role-bottom-nav"', 'id="role-bottom-nav" class="bottom-nav"')

    # 3. Fix inline styles in JS causing overlapping text
    # Remove max-width constraints that are causing the overlap
    html = re.sub(r'max-width:\s*\d+px;?', '', html)
    
    # Bump font sizes and add line-height for readability
    html = re.sub(r'font-size:\s*11px;', 'font-size:12px;line-height:1.5;', html)
    html = re.sub(r'font-size:\s*12px;', 'font-size:13px;line-height:1.5;', html)
    html = re.sub(r'font-size:\s*13px;', 'font-size:14px;line-height:1.5;', html)
    html = re.sub(r'font-size:\s*10px;', 'font-size:12px;line-height:1.5;', html)

    # Specific fix for the Approvals Card (from the user screenshot)
    # The original JS had: 
    # <span class="badge badge-warning" style="margin-bottom:6px;">${ap.type}</span>
    # <p style="font-size:13px;font-weight:600;color:var(--primary);">${ap.details}</p>
    # We want to format this cleanly.
    
    # The badge styling was fine, but let's make sure it's uppercase. 
    # Actually, the user's screenshot showed text looking squished and purple.
    # Let's add a global fix for paragraphs and headers to reset line height
    css_fix = """
    h1, h2, h3, h4, h5, h6 { line-height: 1.3; }
    p { line-height: 1.5; }
    """
    if "h1, h2, h3" not in html:
        html = html.replace('</style>', css_fix + '\n</style>')

    # 4. Improve the icons and clean up button heights
    html = html.replace('height:28px;', 'height:36px;') # Action buttons were too small
    
    # Fix the card display inline styles in JS to add some gap
    html = html.replace('display:flex;justify-content:space-between;align-items:center;', 
                        'display:flex;justify-content:space-between;align-items:center;gap:12px;')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Fixed overlapping text, nav items, and icon design issues!")

if __name__ == '__main__':
    fix_design()
