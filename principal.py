from amazon import Amazon

url = 'https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'
amazon = Amazon(url)
conteudo = amazon.getResponse(amazon.url)
amazon.recuperarProdutos(conteudo)
amazon.recuperarPrecos(conteudo)
amazon.gravarDados('iphone')