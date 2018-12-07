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
import time

def defineVetorDeP():
    # p = []
    # for j in range(1,4):
    #     for i in [5,4.5,4,3.5,3,2.5,2,1.5,1]:
    #         n = i/(10**j)
    #         p.append(n)
    # ps = [0.5, 0.2, 0.1, 5e-2, 2e-2, 1e-2, 5e-3, 2e-3, 1e-3]
    # return ps[:]
    return [0.35826565528689464, 0.3439863398987189, 0.32864110677942393, 0.31223691737656023, 0.29480389353381264, 0.27639977975969465, 0.25711428122884916, 0.23707290714186763, 0.21643983734059555, 0.19541922473480075, 0.17425426837435073, 0.15322337147285262, 0.13263277200537615, 0.11280523992854868, 0.0940648075119953, 0.07671805009999014, 0.06103313724224713, 0.04721864412003856, 0.03540479687870525, 0.025630207542338402, 0.017836996673626204]
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
    dados.defineTaxa(1, 1)
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

    
    # parametros variaveis
    canal_parametro = 'AWGN' # AWGN ou BSC
    modo_parametro = 'euclidiano' # euclidiano, pexata, hamming
    nome_legenda = '_euclid' # Ex. _euclidiano
    nome_arquivo = '_euclid' # Ex. _euclidiano

    # quantidade de bits de informacao a serem enviados. 
    qtdBitsEnviados = int(1e5)
    
    
    codigos = [
        (3, 13, 15, 17),
        (4, 25, 33, 37),
        (6, 117, 127, 155)
    ]

    # define a sequencia aleatória de bits de informacao que se deseja enviar
    enviado = []
    for i in range(qtdBitsEnviados):
        enviado.append(sorteiaBit())

    # itera sobre os codigos possiveis
    for param in codigos:
        codificador = Codificador.Codificador(param[0], param[1], param[2], param[3])
        dados = DadosGrafico.DadosGrafico()
        dados.defineLegend("conv_"+converteParaString(param)+nome_legenda)
        dados.defineTaxa(1, 3)

        print(param)

        # itera sobre todos os valores de p possiveis
        for p in vetorP:
            canal.alteraProbabilidadeDeErro(p)
            canal_gaussiano.alteraVariancia(-1/math.log(2*p)/2)
            codificador.resetCodificador() # reseta as memorias

            decodificador = Decodificador.Decodificador(codificador, mode=modo_parametro, p=p)    
            
            # esse loop decodifica cada subsequencia
            # depois tem que alterar pra decodificar um sequencia inteira
            sequenciaCodificada = []
            for bit in enviado:
                codificado = codificador.codifica(bit) # nesse caso so codifica o bit 0
                sequenciaCodificada.extend(codificado)

            recebido = []
            if canal_parametro == 'AWGN':
                modulado = BPSK.modula(sequenciaCodificada)
                recebido = canal_gaussiano.transmitir(modulado)
            else:
                recebido = canal.transmitir(sequenciaCodificada)

            decodificado = decodificador.decodificaSequencia(recebido)
            # conta os erros de bit
            totalDeErros = contaErros(enviado, decodificado)

            print(p,"    ",totalDeErros/qtdBitsEnviados," ",totalDeErros)

            dados.adicionaPonto(x = p, y = totalDeErros/qtdBitsEnviados)

        dados.salvarEmArquivo('Dados/Novos/conv_'+converteParaString(param)+nome_arquivo+'.txt') # salva os dados em um arquio
        # grafico.adicionaDados(dados, _) # adiciona os dados para plotar depois
