from selenium import webdriver
import time
from bs4 import BeautifulSoup

path = r'/Users/mgobelli/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path = path)
url= "http://www.afa.com.ar/deposito/html/v3/index.html?channel=deportes.futbol.primeraa.448794&lang=es_LA"
driver.maximize_window()
driver.get(url)

ac = driver.find_element_by_class_name("dfMc-Model")
print(ac)

#element = driver.find_element(by=By.ID, value="msjRelatos")


time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
ab = soup.findAll(attrs={"data-id": "172756"})
print(ab)

# <span data-position="2" data-name="Agustín Bouzat" data-id="172756" data-team="away" class="player mc-player" title="" data-original-title="
#       <span class=&quot;name&quot;>Agustín Bouzat</span>">10</span>



    