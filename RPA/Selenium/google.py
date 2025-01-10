from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#import os
#Define o diretório de cache do webdriver-manager
#os.environ['WDM_LOCAL'] = '1'
#os.environ['WDM_CACHE_DIR'] = './drivers_cache'

print('Iniando o robô..')

options = webdriver.ChromeOptions()
options.add_argument("--headless=new") #Executa o Chrome em segundo plano
#options.add_experimental_option("detach", True) # Não encerra o navegado ao final da aplicação.

#Gerencia a versão do Chrome Driver
executable_path = ChromeDriverManager().install()
#driver_path = ChromeDriverManager(path="./meu_diretorio_personalizado").install()

service = ChromeService(executable_path)

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.google.com')


campo = driver.find_element(By.TAG_NAME, 'textarea')
#campo.clear()
campo.send_keys('dolar hoje')
campo.send_keys(Keys.RETURN)

time.sleep(2)

valor_dolar = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(f'Valor do dolar Hoje: {valor_dolar}')

noticias = driver.find_elements(By.TAG_NAME, 'h3')

print('Notícias:')
for noticia  in noticias:
    if noticia.text != '':
        print(noticia.text)


print('Finalizado.')

#time.sleep(10)

driver.quit() #: Use quando você quiser fechar todas as janelas abertas e encerrar completamente a sessão do WebDriver.
#driver.close(): Use quando você quiser fechar apenas a janela atual do navegador, mantendo outras janelas (se existirem) e a sessão do WebDriver ativa