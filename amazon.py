from bs4 import BeautifulSoup
import requests
import sys
from excel import Excel

class Amazon(Excel):
    
    def __init__(self):
        self.excel = Excel()
        
    def getSoup(self, conteudo):
        soup = BeautifulSoup(conteudo, 'html.parser')
        return soup
    
    def recuperarProdutos(self, conteudo):
        ws = self.excel.ws
        wb = self.excel.wb
        count = 1
        soup = self.getSoup(conteudo)
        
        tag_pai = soup.find_all(name='a', attrs={'class':'a-link-normal a-text-normal'})
        nome = soup.find(name='div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-32 sg-col-12-of-20 sg-col-12-of-36 sg-col sg-col-12-of-24 sg-col-12-of-28'})
                
        for d in tag_pai:
            print(count)
            nome = d.find(name='span')
            self.excel.inserirDado(count, 0,nome.text)
            print(nome.text)
            count += 1
            
    def recuperarPrecos(self, conteudo):
        ws = self.excel.ws
        wb = self.excel.wb
        count = 1
        
        soup = self.getSoup(conteudo)
        preco = soup.find(name='span', attrs={'class':'a-price-whole'})
        tag_preco = soup.find_all(name='div', attrs={'class':'sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32'})
        
        
        if len(tag_preco) > 0:
            for d in tag_preco:
                print(count)
                preco = d.find(name='span', attrs={'class':'a-offscreen'})
                if preco is not None:
                    print(preco.text)
                    self.excel.inserirDado(count, 1, preco.text)
                else:
                    self.excel.inserirDado(count, 1, "—")
                    print('nada')
                count += 1
        else:
            tag_preco = soup.find_all(name='div', attrs={'class':'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'})
            for d in tag_preco:
                print(count)
                preco = d.find(name='span', attrs={'data-a-size':'l'})
                
                if preco is not None:
                    preco = preco.findChild()
                    print(preco.text)
                    self.excel.inserirDado(count, 1, preco.text)
                else:
                    self.excel.inserirDado(count, 1, "—")
                    print('nada')
                count += 1
            
    def gravarDados(self, nome):
        self.excel.tabelaEstrutura()
        self.excel.salvarTabela(nome)
        print('dados salvos com sucesso!')