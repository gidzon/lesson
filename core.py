import requests
import os.path
from bs4 import BeautifulSoup


def webPageRequest(url):
    return requests.get(url)


def writePageToFile(response, fileName):
    if not os.path.isfile(fileName):
        html = response.text
        file = open(fileName, 'w')
        file.write(html)
        file.close()

def readPageToFile(fileName):
    file = open(fileName, 'r')
    html = file.read()
    file.close()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('article', class_='newsentry')


def parseContent(emptyList, contents):
    for item in contents:
        title = item.find('a').string
        link = item.find('a').get('href')
        content = item.find('div', class_='newscontent').div.p.string
        emptyList.append({
            'title': title,
            'link': link,
            'content': content,
        })
    return emptyList