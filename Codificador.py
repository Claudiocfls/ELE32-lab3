import Register

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
        for i in str(g):
            if i >= '8' or i<'0':
                print("O parametro nao esta na base octal: ",g)
                return None

        polinomio = "".join([format(int(c), '03b') for c in str(g)])
        polinomio = max(self.m+1-len(polinomio),0)*'0'+polinomio
        polinomio = polinomio[-(self.m+1):]
        polinomio = [int(c) for c in polinomio]
        return polinomio[:]


    def codifica(self, bitInformacao):
        codigo = []
        gpol = [self.g1pol, self.g2pol, self.g3pol]
        for polinomio in gpol:
            cd = bitInformacao*polinomio[0]
            for i in range(self.m):
                cd += polinomio[i+1]*self.register.r[i]
            cd %= 2
            codigo.append(cd)

        self.register.add(bitInformacao)
        return codigo[:] 

    def resetCodificador(self):
        self.register.resetRegister()


if __name__ == '__main__':
    
    # teste
    cod = Codificador(3, 13, 15, 17)
    sequencia = [1,0,1,1,0,1,0,0,0]
    codificado = []
    for bit in sequencia:
        c = cod.codifica(bit)
        codificado.extend(c[:])
    correto = [1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,1]
    if codificado == correto:
        print("codificacao correta")
    else:
        print("DECODIFICACAO INCORRETA!!")