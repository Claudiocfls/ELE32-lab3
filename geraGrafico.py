import DadosGrafico
import Grafico
import os


grafico = Grafico.Grafico()

# arquivos = os.listdir("Dados/ciclico")
# for arquivo in arquivos:
#     dado = DadosGrafico.DadosGrafico()
#     dado.dadosDeArquivo("Dados/ciclico/"+arquivo)
#     grafico.adicionaDados(dado, "")

# arquivos = os.listdir("Dados/linear")
# for arquivo in arquivos:
#     dado = DadosGrafico.DadosGrafico()
#     dado.dadosDeArquivo("Dados/linear/"+arquivo)
#     grafico.adicionaDados(dado, "")

# arquivos = os.listdir("Dados/convolucional")
# for arquivo in arquivos:
#     dado = DadosGrafico.DadosGrafico()
#     dado.dadosDeArquivo("Dados/convolucional/"+arquivo)
#     grafico.adicionaDados(dado, "")

arquivos = os.listdir("Dados/Novos")
arquivos.sort()
for arquivo in arquivos:
    dado = DadosGrafico.DadosGrafico()
    dado.dadosDeArquivo("Dados/Novos/"+arquivo)
    grafico.adicionaDados(dado, "-")

# dado = DadosGrafico.DadosGrafico()
# dado.dadosDeArquivo('Dados/linear/hamming.txt')
# grafico.adicionaDados(dado, "")
# dado.dadosDeArquivo('Dados/ciclico/cicl_1,0,0,0,1,0,1.txt')
# grafico.adicionaDados(dado, "")
# dado.dadosDeArquivo('Dados/convolucional/conv_4,25,33,37.txt')
# grafico.adicionaDados(dado, "")
# dado.dadosDeArquivo('Dados/convolucional/conv_4,25,33,37_pexata.txt')
# grafico.adicionaDados(dado, "")
# dado.dadosDeArquivo('Dados/convolucional/conv_4,25,33,37_euclidiano.txt')
# grafico.adicionaDados(dado, "")



# referencia
dado = DadosGrafico.DadosGrafico()
dado.dadosDeArquivo("Dados/semcodificacao.txt")
grafico.adicionaDados(dado, ".k-")

grafico.mostraGrafico()

