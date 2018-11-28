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
        grafico['rate'] = dadosGrafico.rate
        grafico['legend'] = dadosGrafico.legend
        grafico['style'] = styles
        self.dados[self.index] = copy.deepcopy(grafico)
        self.index += 1

    def mostraGrafico(self):
        plt.figure(1)
        for i in range(self.index):
            dadosTemp = self.dados[i]
            x = [c for c in dadosTemp['x']]
            # y = [math.log10(c) for c in dadosTemp['y']]
            y = [c for c in dadosTemp['y']]
            plt.plot(x,y,label=dadosTemp['legend'])
            # plt.plot(x,y, dadosTemp['style'], label=dadosTemp['legend'])
        plt.legend()
        # plt.xscale('log')
        # plt.yscale('log')
        left,right = plt.xlim()
        plt.xlim(right,left)
        plt.title("Desempenho dos códigos")
        # plt.yscale('log', basey=10)
        plt.xlabel("p")
        plt.ylabel("Probabilidade de erro de bit")

        plt.savefig("grafico_linear.png")
        plt.figure(2)

        # outro grafico
        for i in range(self.index):
            dadosTemp = self.dados[i]
            x = [math.log10(dadosTemp['x'][c]) for c in range(len(dadosTemp['x'])) if dadosTemp['y'][c] != 0]
            y = [math.log10(dadosTemp['y'][c]) for c in range(len(dadosTemp['y'])) if dadosTemp['y'][c] != 0]
            # y = [c for c in dadosTemp['y']]
            plt.plot(x,y,label=dadosTemp['legend'])
            # plt.plot(x,y, dadosTemp['style'], label=dadosTemp['legend'])
        plt.legend()
        # plt.xscale('log')
        # plt.yscale('log')
        left,right = plt.xlim()
        plt.xlim(right,left)
        plt.title("Desempenho dos códigos")
        # plt.yscale('log', basey=10)
        plt.xlabel("log(p)")
        plt.ylabel("log(Probabilidade de erro de bit)")
        
        plt.savefig("grafico_log.png")
        plt.figure(3)

        # Grafico Convertido
        for i in range(self.index):
            dadosTemp = self.dados[i]
            x = [10*math.log10(-math.log(2*dadosTemp['x'][c])/dadosTemp['rate']) for c in range(len(dadosTemp['x'])) if dadosTemp['y'][c] != 0 and dadosTemp['x'][c] != 0.5]
            y = [math.log10(dadosTemp['y'][c]) for c in range(len(dadosTemp['y'])) if dadosTemp['y'][c] != 0 and dadosTemp['x'][c] != 0.5]
            # y = [c for c in dadosTemp['y']]
            plt.plot(x, y, label=dadosTemp['legend'])
            # plt.plot(x,y, dadosTemp['style'], label=dadosTemp['legend'])
        plt.legend()
        # plt.xscale('log')
        # plt.yscale('log')
        # left, right = plt.xlim()
        # plt.xlim(right, left)
        plt.title("Desempenho dos códigos")
        # plt.yscale('log', basey=10)
        plt.xlabel("Ei/N0")
        plt.ylabel("log(Probabilidade de erro de bit)")

        plt.savefig("grafico_convertido.png")
        plt.show()