import requests
from bs4 import BeautifulSoup
import csv
from os.path import exists

CSV = 'cha.txt'
HOST = 'https://hozcity.ru/'
URL = 'https://hozcity.ru/catalog/termopoty/filter/993-is-%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA/apply/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def get_html(url,params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-item')
    cha =[]

    for item in items:
        cha.append(
            {
                'title': item.find('h3', class_='product-item-title').get_text(strip=True),
                'link_product': HOST + item.find('a', class_='product-item-image-wrapper').get('href'),
                'prise': (item.find('span', class_='product-item-price-current').get_text()).replace("\n","") + 'руб.'
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

def parser3():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cha = []
        for page in range(1, PAGENATION+1):
            print(f'Парсим страницу:{page}')
            html = get_html(URL, params={'PAGEN_1': page})
            cha.extend(get_content(html.text))
        save_doc(cha,CSV)
    else:
        print('Error')

#def parser3():
   # html = get_html(URL)
   ## if html.status_code == 200:
     #   print(f'Парсим')
      #  cha = get_content(html.text)
       # save_doc(cha,CSV)
   # else:
    #    print('Error')

#parser3()
#5 стр