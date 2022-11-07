import requests
from bs4 import BeautifulSoup
import pandas as pd

class Dados_IBGE:
    def __init__(self, url):
        self.url = url
        # self.dict_dados_IBGE = {}
        self.lista_dados_IBGE = []

    def pegar_dados(self):
        dados_html = requests.get(self.url)
        self.soup = BeautifulSoup(dados_html.text, 'html.parser')
        self.indicadores = self.buscar_tags('span', 'nonsprite')
        self.ultimos = self.buscar_tags('td', 'ultimo', 'Último')
        self.anteriores = self.buscar_tags('td', 'anterior', 'Anterior')
        self.doze_meses = self.buscar_tags('td', 'dozemeses', '12 meses')
        self.anos = self.buscar_tags('td', 'ano', 'No ano')

        # # Cria um dicionário com todos os dados
        # for index, item in enumerate(self.indicadores):
        #     self.dict_dados_IBGE[item] = {
        #         'último': self.ultimos[index],
        #         'anterior': self.anteriores[index],
        #         '12_meses': self.doze_meses[index],
        #         'ano': self.anos[index]
        #     }

        # Cria uma lista com todos os dados (ficou mais fácil para gerar o csv)
        for index, item in enumerate(self.indicadores):
            self.lista_dados_IBGE.append([self.indicadores[index],
                                          self.ultimos[index],
                                          self.anteriores[index],
                                          self.doze_meses[index],
                                          self.anos[index]])


    def buscar_tags(self, tag, classe, titulo=''):
        self.tag = tag
        self.classe = classe
        self.titulo = titulo
        lista_dados = []
        dados_tag = self.soup.findAll(self.tag, attrs={f"class": {self.classe}})
        for dados in dados_tag:
            lista_dados.append(dados.text.replace(f'{self.titulo}', '').strip())
        return lista_dados


    # def imprimir_dados(self):
        # saida = ''
        # for key, value in self.dict_dados_IBGE.items():
        #     for k, v in value.items():
        #         saida += f'{k}: {v} | '
        #     print(f'{key}: {saida}')
        #     saida = ''


    def gera_csv(self):
        df = pd.DataFrame(self.lista_dados_IBGE, columns=['Indicador', 'Último', 'Anterior', '12 Meses', 'Ano'])
        df.to_csv('dados.csv', index=False)


if __name__ == '__main__':
    app = Dados_IBGE('https://www.ibge.gov.br/indicadores#ipca',)
    app.pegar_dados()
    # app.imprimir_dados()
    app.gera_csv()
