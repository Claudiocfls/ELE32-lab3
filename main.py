import Codificador
import Diagrama
import Decodificador
import CanalBSC

if __name__ == '__main__':
    codificador = Codificador.Codificador(2, 13, 15, 17) # mudar o primeiro parametro para 3 e trocar o codificador
    decodificador = Decodificador.Decodificador(codificador)
    canal = CanalBSC.CanalBSC(0.4)
    qtdBitsEnviados = int(1e5)
    totalDeErros = 0

    for i in range(qtdBitsEnviados):
        a = codificador.codifica(0)
        b,erros = canal.transmitir(a)
        totalDeErros += erros
        decodificador.adicionaSequencia(b)

    decodificado = decodificador.decodificaSequencia()
    decodificado.reverse()
    
    cont = 0
    for i in range(qtdBitsEnviados):
        if 0 != decodificado[i]:
            cont += 1
    print("erros de bit incluidos pelo canal: ",totalDeErros)
    print("erros de bit apos decodificacao: ",cont)
