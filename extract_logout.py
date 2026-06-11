def extract():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    idx = html.find('function logoutUser')
    if idx != -1:
        out = html[idx:idx+400]
        with open('logout_debug.txt', 'w', encoding='utf-8') as out_f:
            out_f.write(out)

if __name__ == '__main__':
    extract()
