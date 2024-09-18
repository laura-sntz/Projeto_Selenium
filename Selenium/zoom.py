from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.zoom.com.br/')

sleep(3)
barra = driver.find_element(By.CLASS_NAME, 'AutoCompleteStyle_autocomplete__BvELB')
input = barra.find_element(By.TAG_NAME, 'input')
input.send_keys('celular')
input.send_keys(Keys.ENTER)

items = len(driver.find_elements_by_class_name("Hits_ProductCard__Bonl_"))
total1 = []

for item in range(items):
    items = driver.find_elements_by_class_name("Hits_ProductCard__Bonl_")
    for item in items:
        c_name = item.find_elements_by_class_name('').txt

driver.close()