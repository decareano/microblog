from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.afa.com.ar/deposito/html/v3/index.html?channel=deportes.futbol.primeraa.448786&lang=es_LA"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
mydivs = soup.find('div')
print(mydivs)







# import bs4 as bs
# import urllib.request
# sauce = urllib.request.urlopen("http://www.afa.com.ar/deposito/html/v3/index.html?channel=deportes.futbol.primeraa.448786&lang=es_LA").read()
# soup = bs.BeautifulSoup(sauce,'lxml')
# list = []
# for div in soup.find_all('div', class_='results-link', limit=10):
#     initialglobenewsnyseurls = ("http://www.afa.com.ar/html/9/estadisticas-de-primera-division" + div.h1.a['href'])
#     list.append(initialglobenewsnyseurls)
#     a, b, c, d, e, f, g, h, i, j = list

# print(list)


