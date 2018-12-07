import Diagrama
import copy
import Codificador
import CanalBSC
import VetorDeEstados
import Trelica

class Decodificador:
    # param: mode -> indica qual modo usar para realizar a decodificacao: euclidiano, pexata, hamming
    def __init__(self, codificador, mode, p=None):
        self.codificador = codificador
        self.mode = mode 
        self.p = p
        self.trelica = Trelica.Trelica(codificador, mode, p)

    def adicionaSubSequencia(self, subsequencia):
        self.trelica.adicionaSubSequencia(subsequencia)

    def decodificaSequencia(self, sequencia):
        if len(sequencia) == 0:
            print("SEQUENCIA VAZIA!!")
            return

        ind = 0
        while ind<len(sequencia):
            self.adicionaSubSequencia(sequencia[ind:ind+3])
            ind += 3

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
            if estado[0] == True:
                if estado[1] <= menorCusto or menorCusto == -1:
                    aux = estado
                    menorCusto = estado[1]
        return aux[-1]



