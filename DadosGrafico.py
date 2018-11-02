import json

class DadosGrafico:
    def __init__(self):
        self.legend = "Sem legenda"
        self.x = []
        self.y = []

    def defineLegend(self, legend):
        self.legend = legend

    def adicionaPonto(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def dadosDeArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, 'r')
        conteudo = arquivo.read()
        
        conteudo = json.loads(conteudo)
        self.legend = conteudo['legend']
        self.x = conteudo['x']
        self.y = conteudo['y']

    def salvarEmArquivo(self, nomeArquivo):
        conteudo = {
            "legend": self.legend,
            "x": self.x,
            "y": self.y
        }
        with open(nomeArquivo, 'w') as outfile:
            json.dump(conteudo, outfile)