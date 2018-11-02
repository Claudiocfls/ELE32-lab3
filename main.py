import Codificador
import Diagrama
import Decodificador
import CanalBSC
import DadosGrafico
import Grafico

def defineVetorDeP():
    p = []
    for j in range(1,2):
        for i in [5,4,3,2]:
            n = i/(10**j)
            p.append(n)
    return p[:]

def converteParaString(param):
    a = ""
    for i in param[:-1]:
        a += str(i)+', '
    a += str(param[-1])
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

    qtdBitsEnviados = int(1e2)
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
            for i in range(qtdBitsEnviados):
                a = codificador.codifica(0) # nesse caso so codifica o bit 0
                b,erros = canal.transmitir(a)
                totalDeErros += erros
                decodificador.adicionaSequencia(b)
            decodificado = decodificador.decodificaSequencia()
            
            # conta os erros de bit
            cont = 0
            for i in range(qtdBitsEnviados):
                if 0 != decodificado[i]: # considerando que so enviou bit 0 de informacao
                    cont += 1

            # print("erros de bit incluidos pelo canal: ",totalDeErros)
            # print("erros de bit apos decodificacao: ",cont)

            print(p,"    ",cont/qtdBitsEnviados)
            dados.adicionaPonto(x = p, y = cont/qtdBitsEnviados)

        dados.salvarEmArquivo(converteParaString(param)+'.txt') # salva os dados em um arquio
        grafico.adicionaDados(dados, styles[ind]) # adiciona os dados para plotar depois
        ind += 1

    adicionaReferencia(vetorP, grafico)

    grafico.mostraGrafico()

