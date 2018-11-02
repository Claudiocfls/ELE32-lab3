import Register
import geraVetor

class Codificador:
    def __init__(self,m,g1,g2,g3):
        self.m = m
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3

        self.g1pol = self.octal2poly(g1)
        self.g2pol = self.octal2poly(g2)
        self.g3pol = self.octal2poly(g3)

        self.register = Register.Register(m)

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

    def codifica(self, bitInformacao): # codificador teste
        v1 = bitInformacao
        
        v2 = bitInformacao + self.register.r[0] + self.register.r[1] + self.register.r[1]
        v2 %= 2

        v3 = bitInformacao + self.register.r[0] + self.register.r[1] + self.register.r[0]
        v3 %= 2

        self.register.add((self.register.r[0]+self.register.r[1]+bitInformacao)%2)
        return [v1,v2,v3] 

    def codifica2(self, bitInformacao): # codificador correto
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
        return [v1,v2,v3]
