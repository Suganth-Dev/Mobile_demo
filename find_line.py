def extract():
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if 'id="parent-chat"' in line:
            print(f"Line: {i+1}")
            break

if __name__ == '__main__':
    extract()
