from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
html = urlopen('http://www.592meiju.com/video/33.html')
bsObj = BeautifulSoup(html.read(), "html.parser")
downList = bsObj.findAll('ul', {'id': 'downul'})
for downul in downList:
    for downli in downul.findAll('li'):
        print(downli.input.attrs['file_name'] + ' :   ' + downli.input.attrs['value'])
    print('--------------------------')
# print()