from selenium import webdriver
import requests
import sys
from amazon import Amazon

class Pesquisa(Amazon):
    
    def __init__(self):
        chromedriver = '/home/daniel/Downloads/chromedriver_linux64/chromedriver'
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get('https://www.amazon.com.br')
            
    def procurarProduto(self, produto):
        print('procurar')
        url = self.driver.current_url
        response = requests.get(url)
        
        print(response.status_code)
        if response.status_code == 200:
            search_input = self.driver.find_element_by_id('twotabsearchtextbox')
            search_input.send_keys(produto)
            search_input.submit()
            
            url = self.driver.current_url
            response = requests.get(url)
            conteudo = response.content
            return conteudo
        else:
            print(response.status_code)
            print('Página não encontrada')
            sys.exit()
        
    
    def finalizar(self):
        self.driver.close()