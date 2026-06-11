import re

def fix_chat():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    chat_css = """
    /* Premium Chat UI */
    .chat-box { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; padding: 20px; padding-bottom: 100px; height: 100%; }
    .chat-bubble { max-width: 80%; padding: 12px 16px; border-radius: 20px; font-size: 14px; line-height: 1.4; position: relative; box-shadow: var(--shadow-sm); }
    .chat-bubble p { margin: 0; color: inherit !important; }
    .chat-bubble.received { background: #FFFFFF !important; color: var(--text) !important; align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid var(--border); }
    .chat-bubble.sent { background: var(--primary) !important; color: #FFFFFF !important; align-self: flex-end; border-bottom-right-radius: 4px; box-shadow: 0 4px 15px rgba(79, 70, 229, 0.2); border: none; }
    .chat-time { font-size: 11px; margin-top: 6px; display: block; opacity: 0.7; text-align: right; }
    .chat-bubble.sent .chat-time { color: rgba(255,255,255,0.8); }
    
    .chat-input-bar { position: absolute; bottom: 0; left: 0; right: 0; padding: 12px 20px; padding-bottom: 24px; background: rgba(255, 255, 255, 0.95) !important; backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-top: 1px solid var(--border); display: flex; gap: 12px; align-items: center; z-index: 250; box-shadow: 0 -10px 30px rgba(79, 70, 229, 0.05); }
    .chat-input-bar .form-input { margin-bottom: 0; background: #F8FAFC !important; border: 1px solid rgba(99, 102, 241, 0.2) !important; padding: 12px 16px; border-radius: 24px; box-shadow: none; color: var(--text) !important; }
    .chat-input-bar .form-input:focus { border-color: var(--primary) !important; box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important; }
    .chat-input-bar .header-btn { width: 44px; height: 44px; border-radius: 50%; background: var(--primary) !important; color: white !important; border: none !important; box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3) !important; transition: transform 0.2s; display: flex; align-items: center; justify-content: center; }
    .chat-input-bar .header-btn:active { transform: scale(0.9); }
    .chat-input-bar .header-btn i { color: white !important; }
    
    /* Ensure screen content fills space properly for absolute positioning of input */
    #parent-chat .screen-content, #teacher-chat .screen-content { padding: 0 !important; height: 100%; position: relative; background: transparent !important; }
    """

    if "/* Premium Chat UI */" not in html:
        html = html.replace('</style>', chat_css + '\n</style>')
        
        # Also let's fix the inline background color on chat screens that was overriding things
        html = html.replace('<div class="screen-content" style="background-color:#EFEFEF;">', '<div class="screen-content">')

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Chat CSS injected.")
    else:
        print("Chat CSS already exists.")

if __name__ == '__main__':
    fix_chat()
