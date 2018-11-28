import numpy as np
class CanalAWGN():

    def __init__(self, variancia):
        self.variancia = variancia

    def transmitir(self, bloco):
        #valor de p(ocorrer erro na transmissao)
        var = self.variancia

        output=[]
        erros = 0
        noise = np.random.normal(0, var, len(bloco))

        for i in range(0,len(bloco)):
            output.append(bloco[i]+noise[i])
            if output[i] != bloco[i]:
                erros += 1

        return output,erros