import re

def premium_ui():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 1. Inject Premium Header and Button CSS
    premium_css = """
    /* Premium Header UI */
    .app-header { 
      padding: 12px 20px; 
      background: rgba(248, 250, 252, 0.85); 
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      display: grid !important; 
      grid-template-columns: 40px 1fr 40px; 
      align-items: center; 
      position: sticky; top: 0; z-index: 50; 
      border-bottom: 1px solid rgba(0,0,0,0.03);
    }
    .app-header h1 { 
      grid-column: 2; 
      text-align: center; 
      font-size: 18px !important; 
      font-weight: 700; 
      color: #0F172A; 
      margin: 0; 
    }
    
    .header-btn { 
      background: #FFFFFF; 
      border: 1px solid rgba(0,0,0,0.05); 
      width: 40px; height: 40px; 
      border-radius: 50%; 
      display: flex; align-items: center; justify-content: center; 
      color: #0F172A; 
      cursor: pointer; 
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
      transition: all 0.2s ease;
    }
    .header-btn:active { transform: scale(0.95); background: #F1F5F9; }
    
    .app-header .header-btn[onclick*="backward"] { grid-column: 1; justify-self: start; }
    .app-header .header-btn[onclick*="toggleLanguage"], .app-header .header-btn[onclick*="bell"] { grid-column: 3; justify-self: end; }
    
    /* Enhance the card shadows and background for a premium look */
    body { background-color: #0F172A; } /* desktop wrapper */
    .screen-deck { background-color: #F8FAFC !important; }
    .screen { background-color: #F8FAFC !important; }
    
    .card {
      background: #FFFFFF !important;
      border: 1px solid rgba(226, 232, 240, 0.8) !important;
      border-radius: 24px !important;
      box-shadow: 0 10px 40px rgba(15, 23, 42, 0.04) !important;
      padding: 24px !important;
    }
    """
    
    if "Premium Header UI" not in html:
        html = html.replace('</style>', premium_css + '\n</style>')

    # 2. Fix inner h1 styling so it centers correctly if it's dual language
    # Sometimes there are two h1 tags (en and ta). The grid places them on top of each other
    # so we need them to share the center column gracefully.
    # The current CSS uses body.lang-tamil .lang-en { display: none !important; }
    # So only one h1 will be displayed at a time. The grid column 2 will work perfectly.

    # Fix lucide icons to make sure they use chevron-left instead of arrow-left for a more modern iOS feel
    html = html.replace('data-lucide="arrow-left"', 'data-lucide="chevron-left" style="width:24px;height:24px;stroke-width:2.5;"')
    
    # Increase general text darkness for premium contrast
    html = html.replace('color:var(--text-muted);', 'color:#64748B;')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Premium UI injected!")

if __name__ == '__main__':
    premium_ui()
