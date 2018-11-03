import DadosGrafico
import Grafico

grafico = Grafico.Grafico()

dados1 = DadosGrafico.DadosGrafico()
dados1.dadosDeArquivo("hamming.txt")
grafico.adicionaDados(dados1, "ro" )

dados1 = DadosGrafico.DadosGrafico()
dados1.dadosDeArquivo("3, 13, 15, 17.txt")
grafico.adicionaDados(dados1, "ro" )

dados1 = DadosGrafico.DadosGrafico()
dados1.dadosDeArquivo("4, 25, 33, 37.txt")
grafico.adicionaDados(dados1, "ro" )

dados1 = DadosGrafico.DadosGrafico()
dados1.dadosDeArquivo("6, 117, 127, 155.txt")
grafico.adicionaDados(dados1, "ro" )

dados1 = DadosGrafico.DadosGrafico()
dados1.dadosDeArquivo("semcodificacao.txt")
grafico.adicionaDados(dados1, "ro" )

grafico.mostraGrafico()

