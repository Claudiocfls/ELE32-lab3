import DadosGrafico
import Grafico
import os


grafico = Grafico.Grafico()

arquivos = os.listdir("Dados/ciclico")
for arquivo in arquivos:
    dado = DadosGrafico.DadosGrafico()
    dado.dadosDeArquivo("Dados/ciclico/"+arquivo)
    grafico.adicionaDados(dado, "")

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


# referencia
dado = DadosGrafico.DadosGrafico()
dado.dadosDeArquivo("Dados/semcodificacao.txt")
grafico.adicionaDados(dado, "k-")

grafico.mostraGrafico()

