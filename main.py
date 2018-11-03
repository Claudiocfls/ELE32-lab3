import Codificador
import Diagrama
import Decodificador
import CanalBSC
import DadosGrafico
import Grafico
import random

def defineVetorDeP():
    p = []
    for j in range(1,2):
        for i in [5,4.5,4,3.5,3,2.5,2,1.5,1]:
            n = i/(10**j)
            p.append(n)
    ps = [0.5, 0.2, 0.1, 5e-2, 2e-2, 1e-2, 5e-3, 2e-3, 1e-3]
    return ps[:]
    return p[:]

def converteParaString(param):
    a = ""
    for i in param[:-1]:
        a += str(i)+', '
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
    for p in vetorP:
        dados.adicionaPonto(p, p)
    dados.salvarEmArquivo('semcodificacao.txt')
    grafico.adicionaDados(dados,'bs:')

if __name__ == '__main__':

    canal = CanalBSC.CanalBSC(0.0)
    vetorP = defineVetorDeP()

    qtdBitsEnviados = int(1e4)
    grafico = Grafico.Grafico()
    
    codigos = [
        (3, 13, 15, 17),
        (6, 117, 127, 155),
        (4, 25, 33, 37)
    ]

    styles = ['ro-','go-','yo-']
    ind = 0

    for param in codigos:
        codificador = Codificador.Codificador(param[0], param[1], param[2], param[3])
        decodificador = Decodificador.Decodificador(codificador)
        dados = DadosGrafico.DadosGrafico()
        dados.defineLegend(converteParaString(param))

        print(param)
        for p in vetorP:
            canal.alteraProbabilidadeDeErro(p)
            codificador.resetCodificador() # reseta as memorias
            totalDeErros = 0
            
            # esse loop decodifica cada subsequencia
            # depois tem que alterar pra decodificar um sequencia inteira
            contTotal = 0
            enviado = []
            for i in range(qtdBitsEnviados):
            # for i in [0, 0, 1, 1, 1]:
                bitParaEnviar = sorteiaBit()
                # bitParaEnviar = i
                enviado.append(bitParaEnviar)
                a = codificador.codifica(bitParaEnviar) # nesse caso so codifica o bit 0
                b,erros = canal.transmitir(a)
                totalDeErros += erros
                decodificador.adicionaSubSequencia(b)
            decodificado = decodificador.decodificaSequencia()

            # conta os erros de bit
            cont = contaErros(enviado, decodificado)
            contTotal += cont
            # print("erros de bit incluidos pelo canal: ",totalDeErros)
            # print("erros de bit apos decodificacao: ",cont)

            print(p,"    ",contTotal/qtdBitsEnviados," ",contTotal)
            dados.adicionaPonto(x = p, y = contTotal/qtdBitsEnviados)

        dados.salvarEmArquivo(converteParaString(param)+'.txt') # salva os dados em um arquio
        grafico.adicionaDados(dados, styles[ind]) # adiciona os dados para plotar depois
        ind += 1

    adicionaReferencia(vetorP, grafico)

    dados = DadosGrafico.DadosGrafico()
    dados.dadosDeArquivo("hamming.txt")

    grafico.adicionaDados(dados, styles[0])

    grafico.mostraGrafico()

