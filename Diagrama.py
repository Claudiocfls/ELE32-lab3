import geraVetor
class Diagrama:
    def __init__(self, codificador):
        self.encod = codificador
        self.estados = geraVetor.geraVetor(self.encod.m)
        self.grafo = {}
        self.montaDiagrama()
        
    def list2bin(self, lista):
        num = int("".join([str(c) for c in lista]),2)
        return num

    def montaDiagrama(self):
        for estado in self.estados:
            self.encod.register.setRegister(estado)
            codigo = self.encod.codifica(0)
            destino = self.encod.register.r 

            self.grafo[self.list2bin(estado)] = {}
            # self.grafo[self.list2bin(estado)][0] = [estado[:],destino[:],0,codigo[:]]
            self.grafo[self.list2bin(estado)][0] = [self.list2bin(destino[:]), codigo[:]]
            
            self.encod.register.setRegister(estado)
            codigo = self.encod.codifica(1)
            destino = self.encod.register.r 
            # self.grafo[self.list2bin(estado)][1] = [estado[:],destino[:],1,codigo[:]]
            self.grafo[self.list2bin(estado)][1] = [self.list2bin(destino[:]), codigo[:]]
        self.encod.register.resetRegister()
        
    def getTransicao(self, estadoAtual, bit):
        return self.grafo[estadoAtual][bit]