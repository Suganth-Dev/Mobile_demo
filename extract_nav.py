import re
def extract():
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    out = []
    for i, line in enumerate(lines):
        if 'bottom-nav' in line:
            out.append(f"{i+1}: {line.strip()}")
            
    with open('nav_debug.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(out))

if __name__ == '__main__':
    extract()
