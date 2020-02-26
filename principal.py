from amazon import Amazon
from pesquisa import Pesquisa

pesquisa = Pesquisa()
produto = 'iphone'
conteudo = pesquisa.procurarProduto(produto)

amazon = Amazon()
amazon.recuperarProdutos(conteudo)
amazon.recuperarPrecos(conteudo)
amazon.gravarDados('produto2')

pesquisa.finalizar()