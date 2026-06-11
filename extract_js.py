import re
def extract():
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    out = "".join(lines[1580:1610])
    with open('nav_js.txt', 'w', encoding='utf-8') as f:
        f.write(out)

if __name__ == '__main__':
    extract()
