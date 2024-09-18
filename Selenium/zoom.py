from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def adicionarProduto(lista):
    itens = (driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_'))
    
    for item in itens:
        cel_nome = item.find_element(By.CLASS_NAME, 'ProductCard_ProductCard_Name__U_mUQ').text
        cel_preco = item.find_element(By.CLASS_NAME, 'Text_MobileHeadingS__HEz7L').text

        produto = ((cel_nome, cel_preco))
        lista.append(produto)

# pontuação com base em que página o produto está
def atribuir_pontuacao(pagina):
    if pagina == 1:
        return 3
    elif pagina == 2:
        return 2
    else:
        return 1

# função que vai rankear os produtos
def rankear_celulares(*listas_pagina):
    #vai fazer um dicionário que só recebe inteiros
    ranking = defaultdict(int)
    
    # i é o índice da sublista por página 
    for i, lista in enumerate(listas_pagina):
        pontuacao_pagina = atribuir_pontuacao(i + 1)  
        
        for celular in lista:
            nome_celular = celular[0]  
            ranking[nome_celular] += pontuacao_pagina
    
    # ordena os celulares por ordem decrescente de pontuação
    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    
    return ranking_ordenado
        
driver = webdriver.Edge()
driver.get('https://www.zoom.com.br/')

# concordando com os termos do site
popup = driver.find_element(By.CLASS_NAME, 'PrivacyPolicy_Button__1RxwB')
popup.click()

sleep(3)
pesquisa = driver.find_element(By.CLASS_NAME, 'AutoCompleteStyle_autocomplete__BvELB')
digitar = pesquisa.find_element(By.TAG_NAME, 'input')
digitar.send_keys('smartphone', Keys.ENTER)

# lista de mais relevante na página 1
sleep(3)
lista_rel1 = []
adicionarProduto(lista_rel1)

sleep(3)
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 2"]')
# tive que fazer por meio do javascript, pois vários métodos não funcionaram para fazer o botão ser clicado
driver.execute_script("arguments[0].click();", botao)

# lista de mais relevante na página 2
sleep(3)
lista_rel2= []
adicionarProduto(lista_rel2)

sleep(3)
# sem declarar de novo a página não funciona
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 3"]')
driver.execute_script("arguments[0].click();", botao)

# lista de mais relevante na página 3
sleep(3)
lista_rel3= []
adicionarProduto(lista_rel3)

# voltando para a página 1
sleep(3)
pagina1 = driver.find_element(By.CLASS_NAME, 'Paginator_page__LYvDd')
botao_volta = pagina1.find_element(By.XPATH, '//a[@aria-label="Página 1"]')
driver.execute_script("arguments[0].click()", botao_volta)

# mudando para menor preço
sleep(3)
selecao = driver.find_element(By.CLASS_NAME, 'Select_Select__1HNob')
menor_preco = selecao.find_element(By.XPATH, '//option[@value="price_asc"]')
menor_preco.click()

# lista de menor preço página 1 | precisa de sleep maior para a página recarregar com o filtro
sleep(10)
lista_preco1 = []
adicionarProduto(lista_preco1)

sleep(3)
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 2"]')
driver.execute_script("arguments[0].click();", botao)

# lista menor preço página 2
sleep(3)
lista_preco2 = []
adicionarProduto(lista_preco2)

sleep(3)
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 3"]')
driver.execute_script("arguments[0].click();", botao)

# lista menor preço página 3
sleep(3)
lista_preco3 = []
adicionarProduto(lista_preco3)

sleep(3)
pagina1 = driver.find_element(By.CLASS_NAME, 'Paginator_page__LYvDd')
botao_volta = pagina1.find_element(By.XPATH, '//a[@aria-label="Página 1"]')
driver.execute_script("arguments[0].click()", botao_volta)

# mudando para melhor avaliado
sleep(3)
selecao = driver.find_element(By.CLASS_NAME, 'Select_Select__1HNob')
melhor_aval = selecao.find_element(By.XPATH, '//option[@value="rating_desc"]')
melhor_aval.click()

# lista melhor avaliado página 1
sleep(10)
lista_avl1 = []
adicionarProduto(lista_avl1)

sleep(3)
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 2"]')
driver.execute_script("arguments[0].click();", botao)

# lista melhor avaliado página 2
sleep(3)
lista_avl2 = []
adicionarProduto(lista_avl2)

sleep(3)
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 3"]')
driver.execute_script("arguments[0].click();", botao)

# lista melhor avaliado página 3
sleep(3)
lista_avl3= []
adicionarProduto(lista_avl3)

# lista geral separada por página
listas_pagina = [
    lista_rel1 + lista_preco1 + lista_avl1,  # página 1
    lista_rel2 + lista_preco2 + lista_avl2,  # página 2
    lista_rel3 + lista_preco3 + lista_avl3   # página 3
]

ranking_final = rankear_celulares(*listas_pagina)

# ranking final
for pos, (celulares, pontos) in enumerate(ranking_final, 1):
    print(f"{pos}. {celulares}: {pontos} pontos")

print('\n', listas_pagina)

driver.close()
