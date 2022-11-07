# Projeto de Aprendizagem

Esse projeto faz parte de meu aprendizado sobre Python com BeautifulSoup.


## Projeto Web Scraping da página de indicadores do IBGE

Projeto foi desenvolvido utilizando as bibliotecas BeautifulSoup e Requests para requisição da página e web scraping, no final utilizado o Pandas para gerar o dataframe e exportar em um csv.

Alguns comandos utilizados:

- Requisição para a página: `requests.get()`
- Conseguir o index em um loop de uma lista: `enumerate()`
- Procurar tags no código html: `BeautifulSoup.findAll()`
