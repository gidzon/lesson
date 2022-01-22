import core

response = core.webPageRequest('https://www.php.net/')
contents = core.readPageToFile('php-net.html')
listResult = core.parseContent([], contents)
