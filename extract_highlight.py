def extract():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    idx = html.find('function updateTabNavigationHighlights')
    if idx != -1:
        print(html[idx:idx+800])

if __name__ == '__main__':
    extract()
