import requests
import os.path
from bs4 import BeautifulSoup

filePath = 'php-net.html'
if not os.path.isfile(filePath):
    url = 'https://www.php.net/'
    response = requests.get(url)
    html = response.text
    file = open('php-net.html', 'w')
    file.write(html)
    file.close()

resultContent = []

file = open('php-net.html', 'r')
html = file.read()
file.close()
soup = BeautifulSoup(html, 'html.parser')
articles = soup.findAll('article', class_='newsentry')


for item in articles:
    title = item.find('a').string
    link = item.find('a').get('href')
    content = item.find('div', class_='newscontent').div.p.string
    resultContent.append({
        'title' : title,
        'link' : link,
        'content' : content,
    })

