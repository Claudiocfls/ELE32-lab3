import Diagrama
import copy
import Codificador
import CanalBSC
import VetorDeEstados
import Trelica

class Decodificador:
    def __init__(self, codificador):
        self.codificador = codificador
        self.trelica = Trelica.Trelica(codificador)

    def adicionaSubSequencia(self, subsequencia):
        self.trelica.adicionaSubSequencia(subsequencia)

    def decodificaSequencia(self):
        if self.trelica.tamanhoTrelica() <= 1:
            print("Eh necessario adicionar subsequencias antes: Ex.: adicionaSubSequencia([0,1,0])")
            return
        estadoFinal = self.__extraiEstadoMenorCusto()
        listaDecodificada = self.trelica.percorreTrelica(estadoFinal)
        listaDecodificada.reverse()
        self.trelica.resetaTrelica()
        return listaDecodificada[:]

    def __extraiEstadoMenorCusto(self):
        vetor = self.trelica.ultimoVetor()
        aux = ()
        menorCusto = -1
        for estado in vetor:
            if estado[1] < menorCusto or menorCusto == -1:
                aux = estado
                menorCusto = estado[1]
        return aux[-1]



