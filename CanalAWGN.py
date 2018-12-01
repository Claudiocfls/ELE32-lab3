import numpy as np

class CanalAWGN():

    def __init__(self, variancia):
        self.variancia = variancia

    def alteraVariancia(self, variancia):
        self.variancia = variancia

    def transmitir(self, bloco):
        
        output=[]
        noise = np.random.normal(0, self.variancia, len(bloco))

        for i in range(0,len(bloco)):
            output.append(bloco[i]+noise[i])
  
        return output