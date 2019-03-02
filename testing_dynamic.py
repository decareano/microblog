import requests
from lxml import html
#http = urllib3.PoolManager()
url = "http://www.afa.com.ar/html/9/estadisticas-de-primera-division"
#soup = BeautifulSoup(r.data, 'html5lib')
#print (soup.title)
#print (soup.title.text)

path = '//*[@id="container"]/table/tbody/tr/td/p[1]/iframe'
response = requests.get(url)
byte_string = response.content
source_code = html.fromstring(byte_string)
tree = xpath(path)
print(tree[0].text_content()) 


