import Codificador
import Diagrama
import Decodificador
import CanalBSC
import CanalAWGN
import DadosGrafico
import Grafico
import random
import ModuladorBPSK
import math

def defineVetorDeP():
    p = []
    for j in range(1,4):
        for i in [5,4.5,4,3.5,3,2.5,2,1.5,1]:
            n = i/(10**j)
            p.append(n)
    # ps = [0.5, 0.2, 0.1, 5e-2, 2e-2, 1e-2, 5e-3, 2e-3, 1e-3]
    # return ps[:]
    return p[:]

def converteParaString(param):
    a = ""
    for i in param[:-1]:
        a += str(i)+','
    a += str(param[-1])
    return a

def contaErros(enviado, recebido):
    cont = 0
    if len(enviado)!=len(recebido):
        print("tamanho incorreto")
    for i in range(len(enviado)):
        if enviado[i]!=recebido[i]:
            cont+=1
    return cont

def sorteiaBit():
    random.seed()
    a = random.randint(0, 1)
    return a 

def adicionaReferencia(vetorP, grafico):
    dados = DadosGrafico.DadosGrafico()
    dados.defineLegend("sem codificacao")
    dados.adicionaRate(1.0)
    for p in vetorP:
        dados.adicionaPonto(p, p)
    dados.salvarEmArquivo('Dados/semcodificacao.txt')
    grafico.adicionaDados(dados,'bs:')

if __name__ == '__main__':

    canal = CanalBSC.CanalBSC(0.0)
    canal_gaussiano = CanalAWGN.CanalAWGN(1)
    vetorP = defineVetorDeP()
    BPSK = ModuladorBPSK.ModuladorBPSK()
    grafico = Grafico.Grafico()

    qtdBitsEnviados = int(1e4)
    
    
    codigos = [
        (3, 13, 15, 17),
        (6, 117, 127, 155),
        (4, 25, 33, 37)
    ]

    # itera sobre os codigos possiveis
    for param in codigos:
        codificador = Codificador.Codificador(param[0], param[1], param[2], param[3])
        dados = DadosGrafico.DadosGrafico()
        dados.defineLegend("conv_"+converteParaString(param)+"_euclidiano")
        dados.defineTaxa(1, 3)

        print(param)
        # itera sobre todos os valores de p possiveis
        for p in vetorP[1:]:
            # canal.alteraProbabilidadeDeErro(p)
            canal_gaussiano.alteraVariancia(-1/math.log(2*p))
            codificador.resetCodificador() # reseta as memorias
            decodificador = Decodificador.Decodificador(codificador, mode='euclidiano')    
            totalDeErros = 0
            
            # esse loop decodifica cada subsequencia
            # depois tem que alterar pra decodificar um sequencia inteira
            contTotal = 0
            enviado = []
            for i in range(qtdBitsEnviados):
                bitParaEnviar = sorteiaBit()
                enviado.append(bitParaEnviar)
                codificado = codificador.codifica(bitParaEnviar) # nesse caso so codifica o bit 0
                modulado = BPSK.modula(codificado)
                recebido = canal_gaussiano.transmitir(modulado)
                decodificador.adicionaSubSequencia(recebido)
            decodificado = decodificador.decodificaSequencia()

            # conta os erros de bit
            cont = contaErros(enviado, decodificado)
            contTotal += cont

            print(p,"    ",contTotal/qtdBitsEnviados," ",contTotal)

            dados.adicionaPonto(x = p, y = contTotal/qtdBitsEnviados)

        dados.salvarEmArquivo('Dados/convolucional/conv_'+converteParaString(param)+'_euclidiano.txt') # salva os dados em um arquio
        # grafico.adicionaDados(dados, _) # adiciona os dados para plotar depois
