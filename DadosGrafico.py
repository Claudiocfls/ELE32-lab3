import json

class DadosGrafico:
    def __init__(self):
        self.legend = "Sem legenda"
        self.x = []
        self.y = []
        self.N = None 
        self.K = None

    def defineLegend(self, legend):
        self.legend = legend

    def defineTaxa(self,K,N):
        self.K = K
        self.N = N

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
        self.N = conteudo['N']
        self.K = conteudo['K']

    def salvarEmArquivo(self, nomeArquivo):
        conteudo = {
            "legend": self.legend,
            "x": self.x,
            "y": self.y,
            "N": self.N,
            "K": self.K
        }
        with open(nomeArquivo, 'w') as outfile:
            json.dump(conteudo, outfile)