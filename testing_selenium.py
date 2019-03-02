from selenium import webdriver
path = r'/Users/mgobelli/Downloads/chromedriver'
browser = webdriver.Chrome(executable_path = path)
browser.get('http://www.afa.com.ar/html/9/estadisticas-de-primera-division')