from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

fil = file.open

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='chromedriver')

current_page = 'http://www.extendasystem.no/meny-pick-and-collect/' #dummylink

table_id = self.driver.find_element(By.ID, 'Ikke_Plukket')
rows = table_id.find_elements(By.TAG_NAME, 'tr')

for row in rows:
    num_of_product = row.find_element_by_tag_name('td')[0]
    product_name = row.find_element_by_tag_name('td')[1]
    product_code = row.find_element_by_tag_name('td')[3]
    replacement = row.find_element_by_tag_name('td')[4]
    fil.write(num_of_product, product_name, product_code, replacement)
