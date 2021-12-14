import requests
from bs4 import BeautifulSoup
import csv
from os.path import exists

CSV = 'cha.txt'
HOST = 'https://www.leran.pro/'
URL = 'https://www.leran.pro/cat/kuhonnaya_tehnika/chainiki_elektricheskie/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def get_html(url,params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item-catalogue catalogue-list-item')
    cha =[]

    for item in items:
        cha.append(
            {
                'title': item.find('a', class_='link link_theme_item-catalogue link_size_l item-catalogue__item-name-link').get_text(strip=True),
                'link_product': HOST + item.find('a', class_='link link_theme_item-catalogue link_size_l item-catalogue__item-name-link').get('href'),
                'prise': (item.find('div', class_='price__row price__row_current text_bold text').get_text()).replace("\n","")
            }
        )
    return cha

def save_doc(items, path):
    if exists(path):
        file = open(path, 'a', newline='')
        writer = csv.writer(file, delimiter=';')
    else:
        file = open(path, 'w', newline='')
        writer = csv.writer(file, delimiter=';')

    for item in items:
        writer.writerow([item['title'],' '])
        writer.writerow([item['link_product'],' '])
        writer.writerow([item['prise'],' '])


def parser2():
    html = get_html(URL)
    if html.status_code == 200:
        print(f'Парсим')
        cha = get_content(html.text)
        save_doc(cha,CSV)
    else:
        print('Error')


#parser2()