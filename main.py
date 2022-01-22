import core

fileName = 'php-net.html'
response = core.webPageRequest('https://www.php.net/')
core.writePageToFile(response, fileName)
contents = core.readPageToFile(fileName)
listResult = core.parseContent([], contents)
