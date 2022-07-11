"""
Домашка до среды:
Распарсить страничку https://teachmeskills.by/kursy-programmirovaniya/obuchenie-python-online
Получить оттуда все темы уроков и вывести в формате (*используя датакласс, читаем про метод asdict):
[
    {
        title (общая тема урока),
        subtitles: [] (подтемы урока)
    }
]"""


from dataclasses import dataclass, asdict
from bs4 import BeautifulSoup
import requests
import json


def main(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


URL = 'https://teachmeskills.by/kursy-programmirovaniya/obuchenie-python-online'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
html = main(URL)

@dataclass
class Topic:
    title: str
    subtitles: list[str]


def adresse(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='t517__sectioninfowrapper')
    themes = []


    for item in items:
        title = item.find('div', class_='t-name').text
        subtitles_elements = item.find_all('li')

        themes.append(Topic(
            title,
            list(map(lambda x: x.text.strip(), subtitles_elements)),
        ))

    print(
        json.dumps(
            list(map(lambda x: asdict(x), themes)),
            indent=4,
            ensure_ascii=False,
        )
    )


if __name__ == '__main__':
    adresse(html.text)