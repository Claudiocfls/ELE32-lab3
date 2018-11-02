class VetorDeEstados:
    def __init__(self, tamanho):
        self.tamanho = tamanho 
        self.vetor = []
        self.__criaVetor()

    def __criaVetor(self):
        foiAtingido = False
        custoTotal = 0
        bitTransicao = -1
        estadoAnterior = -1
        estadoAtual = 0
        for i in range(self.tamanho):
            self.vetor.append((foiAtingido,custoTotal,bitTransicao,estadoAnterior,i))
