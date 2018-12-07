import Diagrama
import copy
import VetorDeEstados
import math

class Trelica:
    def __init__(self, codificador, modo, p=None):
        self.qtdEstados = 2**codificador.m
        self.diagrama = Diagrama.Diagrama(codificador)
        self.trelica = self.__iniciaTrelica()
        self.qtdEstadosAtingidos = 0
        self.modo = modo
        self.p = p

    def adicionaSubSequencia(self, subSequenciaCodigo):
        vetorAnterior = self.trelica[-1]
        novoVetor = VetorDeEstados.VetorDeEstados(self.qtdEstados)
        estadosJaAtingidos = self.__getEstadosJaAtingidos(vetorAnterior)
        for estadoAnterior in estadosJaAtingidos:
            for bit in [0,1]:
                transicao = self.diagrama.getTransicao(estadoAnterior[-1], bit)
                destino = transicao[0]
                custoAnterior = estadoAnterior[1]
                custoDaTransicao = self.__defineCusto(subSequenciaCodigo, transicao[1])
                self.__updateNovoVetor(novoVetor, estadoAnterior[-1], destino, custoDaTransicao, bit, custoAnterior)
        self.trelica.append(copy.deepcopy(novoVetor))
    
    def ultimoVetor(self):
        return self.trelica[-1].vetor

    def tamanhoTrelica(self):
        return len(self.trelica)

    def percorreTrelica(self, estadoFinal):
        percurso = []
        for estados in self.trelica[:0:-1]:
            percurso.append(estados.vetor[estadoFinal][2])
            estadoFinal = estados.vetor[estadoFinal][3]
        return percurso[:]

    def resetaTrelica(self):
        self.qtdEstadosAtingidos = 0
        self.trelica = self.__iniciaTrelica()

    def printaTrelica(self):
        for i in self.trelica:
            print(i.vetor)

    def __iniciaTrelica(self):
        # comeca do estado inical 0
        vetor = VetorDeEstados.VetorDeEstados(self.qtdEstados)
        vetor.vetor[0] = (True,0,0,0,0)
        return [copy.deepcopy(vetor)]

    def __updateNovoVetor(self, novoVetor, origem, destino, custoTransicao, bit, custoAnterior):
        valorAntigo = novoVetor.vetor[destino]
        novoValor = valorAntigo
        if valorAntigo[0] == False:
            novoValor = (True, custoAnterior+custoTransicao, bit, origem, destino)
        else:
            if(self.modo != 'pexata'):
                if valorAntigo[1] >= custoAnterior + custoTransicao:
                    novoValor = (True, custoAnterior+custoTransicao, bit, origem, destino)
            else:
                if valorAntigo[1] >= custoAnterior + custoTransicao:
                    novoValor = (True, custoAnterior+custoTransicao, bit, origem, destino)
        novoVetor.vetor[destino] = novoValor[:]

    def __getEstadosJaAtingidos(self, vetorAnterior):
        if self.qtdEstadosAtingidos == self.qtdEstados:
            return vetorAnterior.vetor
        lista = []
        for estado in vetorAnterior.vetor:
            if estado[0] == True:
                lista.append(estado)
        self.qtdEstadosAtingidos = len(lista)
        return lista

    def __defineCusto(self, a, b):
        if self.modo == 'hamming':
            return self.__distanciaHamming(a, b)
        if self.modo == 'pexata':
            if self.p == None:
                print("NECESSARIO DEFINIR UM VALOR DE PROBABILIDAE DE ERRO PARA O CANAL!")
                return
            return self.__probabilidadeExata(a, b, self.p)
        if self.modo == 'euclidiano':
            return self.__distanciaEuclidiana(a, b)
        print("MODO INCORRETO!")

    def __distanciaHamming(self, a, b):
        distancia = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                distancia += 1
        return distancia

    def __probabilidadeExata(self, a, b, p):
        probabilidade = 1
        for i in range(len(a)):
            if a[i] != b[i]:
                probabilidade *= p
            else:
                probabilidade *= (1-p)
        if probabilidade == 0:
            return 1e6
        return abs(math.log10(probabilidade))

    def __distanciaEuclidiana(self, a, b):
        distanciaQuadrada = 0
        for i in range(len(a)):
            if b[i] == 0:
                c = -1
                distanciaQuadrada = distanciaQuadrada + (a[i]-c)**2
            else:
                c = +1
                distanciaQuadrada = distanciaQuadrada + (a[i]-c)**2
        return math.sqrt(distanciaQuadrada)