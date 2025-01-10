from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#import pdb

print('Iniciando o robô...')

df = pd.read_excel('Files\\dominios.xlsx')
dominios = df.DOMINIOS.values

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new") Não funciona para esse site

executable_path = ChromeDriverManager().install()

service = ChromeService(executable_path)

driver = webdriver.Chrome(service=service, options=options)

driver = webdriver.Chrome()

driver.get('https://registro.br')

dados = []

for dominio in dominios:
    pesquisa = driver.find_element(By.ID, 'is-avail-field')
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultado = driver.find_elements(By.TAG_NAME, 'strong')
    dados.append({'Dominio': dominio, 'Situação': resultado[2].text})
    print(f'Dominio {dominio} {resultado[2].text}')    

res = pd.DataFrame(dados)
res.to_excel('Files\\resultado.xlsx', index = False)    

print("Finalizado.")

#pdb.set_trace()
driver.quit()