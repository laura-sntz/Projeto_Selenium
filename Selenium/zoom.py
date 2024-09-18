from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def adicionarProduto(lista):
    itens = len(driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_'))
    
    for item in range(itens):
        itens = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')
    for item in itens:
        cel_nome = item.find_element(By.CLASS_NAME, 'ProductCard_ProductCard_Name__U_mUQ').text
        avaliacao = item.find_element(By.CLASS_NAME, 'ProductCard_ProductCard_Rating__kCx7o').text
        cel_avaliacao = avaliacao[:3]
        cel_preco = item.find_element(By.CLASS_NAME, 'Text_MobileHeadingS__HEz7L').text
        
        produto = ((cel_nome, cel_avaliacao, cel_preco))
        lista.append(produto)
        
    print(lista)
    print()

driver = webdriver.Edge()
driver.get('https://www.zoom.com.br/')

#concordando com os termos do site
sleep(3)
popup = driver.find_element(By.CLASS_NAME, 'PrivacyPolicy_Button__1RxwB')
popup.click()

sleep(3)
pesquisa = driver.find_element(By.CLASS_NAME, 'AutoCompleteStyle_autocomplete__BvELB')
digitar = pesquisa.find_element(By.TAG_NAME, 'input')
digitar.send_keys('celular', Keys.ENTER)

#lista dos recomendados na página 1
sleep(3)
lista1 = []
adicionarProduto(lista1)

sleep(3)
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 2"]')
#tive que fazer por meio do javascript, pois vários métodos não funcionaram para fazer o botão ser clicado
driver.execute_script("arguments[0].click();", botao)

driver.close()
