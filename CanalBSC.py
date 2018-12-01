import random
# escrito por Toshio
class CanalBSC():

    def __init__(self, probabilidadeDeErro):
        self.probabilidadeDeErro = probabilidadeDeErro

    def alteraProbabilidadeDeErro(self, p):
        self.probabilidadeDeErro = p

    def transmitir(self, bloco):
        #valor de p(ocorrer erro na transmissao)
        p = self.probabilidadeDeErro

        #inicia nova seed para os numeros aleatorios
        random.seed()

        output=[]
        erros = 0
        for i in range(0,len(bloco)):
            aleatorio = random.uniform(0,100)
            if aleatorio <= p*100:
                erros+=1
                if bloco[i] == 1:
                    output.append(0) 
                else: 
                    output.append(1)
            else:
                output.append(bloco[i])

        # return output,erros
        return output