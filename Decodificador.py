import Diagrama
import copy
import Codificador
import CanalBSC
import VetorDeEstados

class Decodificador:
    def __init__(self, codificador):
        self.qtdEstados = 2**codificador.m
        self.qtdMemorias = codificador.m
        self.diagrama = Diagrama.Diagrama(codificador)
        self.k = 0
        self.trelica = self.__iniciaTrelica()
        self.qtdEstadosAtingidos = 0

    def __iniciaTrelica(self):
        # comeca do estado inical 0
        vetor = VetorDeEstados.VetorDeEstados(self.qtdEstados)
        vetor.vetor[0] = (True,0,0,0,0)
        return [copy.deepcopy(vetor)]
        
    def adicionaSequencia(self, subSequenciaCodigo):
        vetorAnterior = self.trelica[-1]
        novoVetor = VetorDeEstados.VetorDeEstados(self.qtdEstados)
        estadosJaAtingidos = self.__getEstadosJaAtingidos(vetorAnterior)
        for estadoAnterior in estadosJaAtingidos:
            for bit in [0,1]:
                transicao = self.diagrama.getTransicao(estadoAnterior[-1], bit)
                destino = transicao[0]
                custoAnterior = estadoAnterior[1]
                custoDaTransicao = self.__distanciaHamming(subSequenciaCodigo, transicao[1])
                self.__updateNovoVetor(novoVetor, estadoAnterior[-1], destino, custoDaTransicao, bit, custoAnterior)
        self.k += 1
        self.trelica.append(copy.deepcopy(novoVetor))
        # print("trelica")
        # self.printaTrelica()

    def decodificaSequencia(self):
        if len(self.trelica) == 0:
            print("Eh necessario adicionar subsequencias antes: Ex.: adicionaSequencia([0,1,0])")
            return

        listaDecodificada = []
        estadoAtual = self.__extraiEstadoMenorCusto()
        for estados in self.trelica[:0:-1]:
            listaDecodificada.append(estados.vetor[estadoAtual][2])
            estadoAtual = estados.vetor[estadoAtual][3]
        listaDecodificada[:].reverse()

        self.trelica = self.__iniciaTrelica()

        return listaDecodificada

    def __extraiEstadoMenorCusto(self):
        vetor = self.trelica[-1].vetor 
        aux = ()
        menorCusto = -1
        for estado in vetor:
            if estado[1] < menorCusto or menorCusto == -1:
                aux = estado
                menorCusto = estado[1]
        return aux[-1]

    def printaTrelica(self):
        for i in self.trelica:
            print(i.vetor)

    def __updateNovoVetor(self, novoVetor, origem, destino, custoTransicao, bit, custoAnterior):
        valorAntigo = novoVetor.vetor[destino]
        novoValor = valorAntigo
        if valorAntigo[0] == False:
            novoValor = (True, custoAnterior+custoTransicao, bit, origem, destino)
        else:
            if valorAntigo[1] > custoAnterior + custoTransicao:
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

    def __distanciaHamming(self, a, b):
        distancia = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                distancia += 1
        return distancia

