import xlwt

class Excel:
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Amazon Produtos')
    style = xlwt.easyxf('font: bold on')
    
    def tabelaEstrutura(self):
        self.ws.write(0,0,'PRODUTO', self.style)
        self.ws.write(0,1,'PREÇO', self.style)

    def salvarTabela(self, nome):
        self.wb.save(nome + '.xls')
        
    def inserirDado(self,count,posicao,dado):
        self.ws.write(count,posicao,dado)