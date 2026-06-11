def extract():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            if 'function renderBottomTabNav' in line:
                print(f"Found function renderBottomTabNav at line {i}")
                print("".join(lines[i:i+80]))
                break
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    extract()
