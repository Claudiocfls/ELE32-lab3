import matplotlib.pyplot as plt
import math
import copy

class Grafico:
    def __init__(self):
        self.dados = {}
        self.index = 0

    def adicionaDados(self, dadosGrafico, styles):
        grafico = {}
        grafico['x'] = dadosGrafico.x
        grafico['y'] = dadosGrafico.y
        grafico['N'] = dadosGrafico.N
        grafico['K'] = dadosGrafico.K
        grafico['legend'] = dadosGrafico.legend
        grafico['style'] = styles
        self.dados[self.index] = copy.deepcopy(grafico)
        self.index += 1

    def mostraGrafico(self):
        plt.figure(1)
        # Grafico linear
        for i in range(self.index):
            dadosTemp = self.dados[i]
            x = [c for c in dadosTemp['x']]
            y = [c for c in dadosTemp['y']]
            plt.plot(x,y, dadosTemp['style'], label=dadosTemp['legend'])
        plt.legend()
        left,right = plt.xlim()
        plt.xlim(right,left)
        plt.title("Desempenho dos códigos")
        plt.xlabel("p")
        plt.ylabel("Probabilidade de erro de bit")
        plt.savefig("Graficos/grafico_linear.png")


        plt.figure(2)
        # Grafico log log
        for i in range(self.index):
            dadosTemp = self.dados[i]
            x = [math.log10(dadosTemp['x'][c]) for c in range(len(dadosTemp['x'])) if dadosTemp['y'][c] != 0]
            y = [dadosTemp['y'][c] for c in range(len(dadosTemp['y'])) if dadosTemp['y'][c] != 0]
            plt.plot(x,y, dadosTemp['style'], label=dadosTemp['legend'])
        plt.legend()
        plt.yscale('log')
        plt.grid()
        left,right = plt.xlim()
        plt.xlim(right,left)
        plt.title("Desempenho dos códigos")
        plt.xlabel("log10(p)")
        plt.ylabel("log10(Probabilidade de erro de bit)")
        plt.savefig("Graficos/grafico_log.png")


        plt.figure(3)
        # Grafico Ei/N0
        for i in range(self.index):
            dadosTemp = self.dados[i]
            rate = dadosTemp['K']/dadosTemp['N']
            x = [10*math.log10(-math.log(2*dadosTemp['x'][c])/rate) for c in range(len(dadosTemp['x'])) if dadosTemp['y'][c] != 0]
            y = [dadosTemp['y'][c] for c in range(len(dadosTemp['y'])) if dadosTemp['y'][c] != 0 ]
            plt.plot(x,y, dadosTemp['style'],label=dadosTemp['legend'])
        # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.legend()
        # plt.grid(which="both")
        plt.grid()
        plt.yscale('log')
        plt.title("Desempenho dos códigos")
        plt.xlabel("Ei/N0(dB)")
        plt.ylabel("log10(Probabilidade de erro de bit)")
        plt.savefig("Graficos/grafico_EiN0.png")


        # ps = []
        # for i in [10,100,1000,10000]:
        #     for j in [5,4,3,2,1]:
        #         ps.append(j/i)
        # ps = ps[1:]
        # plt.figure(4)
        # # Grafico Ei/N0
        # rate = 1
        # y = [math.log10(c) for c in ps]
        # x = [10*math.log10(-math.log(2*c)/rate) for c in ps]
        # plt.plot(x,y)
        
        # plt.legend()
        # plt.grid()
        # plt.title("Desempenho dos códigos")
        # plt.xlabel("Ei/N0(dB)")
        # plt.ylabel("log(p)")


        plt.show()