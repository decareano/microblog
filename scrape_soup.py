from bs4 import BeautifulSoup
import requests
page_link = 'http://www.afa.com.ar/html/9/estadisticas-de-primera-division'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
textContent = []
for i in range(0, 150):
    paragraphs = page_content.find_all("a href")[i].text
    textContent.append(paragraphs)
