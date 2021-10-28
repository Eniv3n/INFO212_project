# 2nd iterationfrom selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='chromedriver')

current_page = 'http://www.extendasystem.no/meny-pick-and-collect/' #dummylink

table_id = self.driver.find_element(By.ID, 'Ikke_Plukket')
rows = table_id.find_elements(By.TAG_NAME, 'tr')

notPicked = []
picked = []

for row in rows:

    num_of_product = str(row.find_element_by_tag_name('td')[0])
    product_name = str(row.find_element_by_tag_name('td')[1])
    product_code = str(row.find_element_by_tag_name('td')[3])
    replacement = str(row.find_element_by_tag_name('td')[4])

    productInfo = [num_of_product, product_name, product_code, replacement]

    if productInfo[0] == "0":
        picked.append(productInfo)
    else:
        notPicked.append(productInfo)

fil = open("notPicked.txt", "w")

if len(notPicked) > 0:
    for i in notPicked:
        fil.write(i[0]," - ",i[1]," - ",i[2]," - ",i[3])

fil.close()
