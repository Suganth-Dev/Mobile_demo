import re

def find_screens():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    matches = re.finditer(r'<div class="screen"[^>]*id="([^"]+)"', html)
    for m in matches:
        print(m.group(1))

if __name__ == '__main__':
    find_screens()
