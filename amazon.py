from bs4 import BeautifulSoup
import requests
import sys
from excel import Excel

class Amazon(Excel):
    
    def __init__(self, url):
        self.url = url
        self.excel = Excel()
        
    def getResponse(self, url):
        response = requests.get(url)
        
        if response.status_code == 200:
            print(response.status_code)
            print('conectado')
            conteudo = response.content
            return conteudo
        
        else:
            print(response.status_code)
            print('Página não encontrada')
            sys.exit()
    
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
        preco = soup.find(name='span', attrs={'class':'a-price-whole'})
        tag_preco = soup.find_all(name='div', attrs={'class':'sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32'})
        
        for d in tag_pai:
            print(count)
            nome = d.find(name='span')
            #ws.write(count,0,nome.text)
            self.excel.inserirDado(count, 0,nome.text)
            print(nome.text)
            count += 1
            
    def recuperarPrecos(self, conteudo):
        ws = self.excel.ws
        wb = self.excel.wb
        count = 1
        
        soup = self.getSoup(conteudo)
        
        tag_pai = soup.find_all(name='a', attrs={'class':'a-link-normal a-text-normal'})
        nome = soup.find(name='div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-32 sg-col-12-of-20 sg-col-12-of-36 sg-col sg-col-12-of-24 sg-col-12-of-28'})
        preco = soup.find(name='span', attrs={'class':'a-price-whole'})
        tag_preco = soup.find_all(name='div', attrs={'class':'sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32'})
        
        for d in tag_preco:
            print(count)
            preco = d.find(name='span', attrs={'class':'a-offscreen'})
            if preco is not None:
                print(preco.text)
                #ws.write(count,1,preco.text)
                self.excel.inserirDado(count, 1, preco.text)
            else:
                #ws.write(count,1,"—")
                self.excel.inserirDado(count, 1, "—")
                print('nada')
            count += 1
        
    def gravarDados(self, nome):
        self.excel.tabelaEstrutura()
        self.excel.salvarTabela(nome)
        print('dados salvos com sucesso!')