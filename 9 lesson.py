# Команды в терминале
# source venv/bin/activate -  в терминале выходим из собственного окружения
# deactivate - выходим из собств. окруж
# pip list проверить каталоги
# pip install ... - устанавливаем библиотеку

import requests
from bs4 import BeautifulSoup

def get_html(url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'}
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    # print(response.text)
    # with open('index.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)
    return response.text

def get_weather(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find_all('div', class_='dates short-d')[0].text
    pass

# soup.find
# soup.find_all

URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
html = get_html(url=URL)
get_weather(html)
