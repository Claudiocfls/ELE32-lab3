import register
import geraVetor
class codificador:
    def __init__(self,m,g1,g2,g3):
        self.m = m
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3

        self.g1pol = self.octal2poly(g1)
        self.g2pol = self.octal2poly(g2)
        self.g3pol = self.octal2poly(g3)

        self.register = register.register(m)

    def octal2poly(self, g):
        a = []
        unidades = g%10
        g = g//10
        dezenas = g%10  
        centenas = g//10

        a = []
        for i in range(3):
            a.append(unidades%2)
            unidades = unidades//2
        a.reverse()

        b = []
        for i in range(3):
            b.append(dezenas%2)
            dezenas = dezenas//2
        b.reverse()

        c = []
        for i in range(3):
            c.append(centenas%2)
            centenas = centenas//2
        c.reverse()

        d = []
        d.extend(c)
        d.extend(b)
        d.extend(a)
        
        d = d[-(self.m+1):]
        return d[:]

    def codifica(self, bitInformacao):
        v1 = bitInformacao
        for i in range(self.m):
            v1 += self.g1pol[i]*self.register.r[i]
        v1 %= 2 

        v2 = bitInformacao
        for i in range(self.m):
            v2 += self.g2pol[i]*self.register.r[i]
        v2 %= 2 

        v3 = bitInformacao
        for i in range(self.m):
            v3 += self.g3pol[i]*self.register.r[i]
        v3 %= 2

        self.register.add(bitInformacao)
        # print(self.register.r)
        # print(v1,v2,v3)
        return [v1,v2,v3]

class diagrama:
    def __init__(self,m, g1,g2,g3):
        self.encod = codificador(m, g1, g2, g3)
        self.estados = geraVetor.geraVetor(m)
        # self.grafo = []
        self.grafo = {}
        self.montaDiagrama()
        
    def list2bin(self, lista):
        num = 0
        for i in range(-1,-len(lista)-1,-1):
            num += lista[i]*2**(-i-1)
        return num

    def montaDiagrama(self):
        for estado in self.estados:
            self.encod.register.setRegister(estado)
            codigo = self.encod.codifica(0)
            destino = self.encod.register.r 

            self.grafo[self.list2bin(estado)] = {}
            self.grafo[self.list2bin(estado)][0] = [estado[:],destino[:],0,codigo[:]]
            
            self.encod.register.setRegister(estado)
            codigo = self.encod.codifica(1)
            destino = self.encod.register.r 
            self.grafo[self.list2bin(estado)][1] = [estado[:],destino[:],1,codigo[:]]

        for i in self.grafo.keys():
            print(self.grafo[i][0])
            print(self.grafo[i][1])

if __name__ == '__main__':
    cod = codificador(3, 13, 15, 17)
    diagra = diagrama(3, 13, 15, 17)