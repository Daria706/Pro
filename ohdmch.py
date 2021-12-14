import requests
from bs4 import BeautifulSoup
import csv
from os.path import exists

CSV = 'cha.txt'
HOST = 'https://www.ohdm.ru/'
URL = 'https://www.ohdm.ru/tovary/k-18127562-chaynik'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def get_html(url,params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='copmany-product-gallery-item')
    cha =[]

    for item in items:
        cha.append(
            {
                'title': item.find('a', class_='cpgi-title').get_text(strip=True),
                'link_product': item.find('a', class_='cpgi-image-link').get('href'),
                'prise': (item.find('div', class_='cpgi-price').get_text()).replace("\n","")
            }
        )
    return cha

def save_doc(items, path):
    file = open(path, 'w', newline='')
    writer = csv.writer(file, delimiter=';')
    for item in items:
        writer.writerow([item['title'],' '])
        writer.writerow([item['link_product'],' '])
        writer.writerow([item['prise'],' '])

def parser1():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cha = []
        for page in range(1, PAGENATION+1):
            print(f'Парсим страницу:{page}')
            html = get_html(URL, params={'page': page})
            cha.extend(get_content(html.text))
        save_doc(cha,CSV)
    else:
        print('Error')

#parser1()
#33 стр