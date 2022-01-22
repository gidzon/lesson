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
else:
    file = open('php-net.html', 'r')
    html = file.read()
    file.close()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

