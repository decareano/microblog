from selenium import webdriver
import time
from bs4 import BeautifulSoup

path = r'/Users/mgobelli/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path = path)
url= "http://www.afa.com.ar/deposito/html/v3/index.html?channel=deportes.futbol.primeraa.448786&lang=es_LA"
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")



#driver.quit()