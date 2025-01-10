from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
#import pdb

print('Iniciando o robô...')

class BotYoutube():
    def __init__(self):
        options = webdriver.ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        
    def busca(self, busca, paginas):
        pagina = 1
        url = f'https://www.youtube.com/results?search_query={busca}'
        self.driver.get(url)
        
        while pagina <= paginas:       
           titulos = self.driver.find_elements(By.XPATH, '//*[@id="video-title"]')
           for titulo in titulos:
               if(titulo.text != ''):
                   print(f'Vídeos encotrado: {titulo.text}')
           self.proxima_pagina(pagina)
           pagina += 1
                   
        self.driver.quit()
    
    def proxima_pagina(self, pagina):
        print(f'Mudando para página {pagina + 1}')
        bottom = pagina * 10000
        self.driver.execute_script(f'window.scrollTo(0,{bottom});')
        time.sleep(5)
        
        

bot = BotYoutube()

bot.busca('Teste', 3)

print('Finalizado.')