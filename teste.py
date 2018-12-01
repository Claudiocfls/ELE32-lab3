import DadosGrafico

dados = DadosGrafico.DadosGrafico()
dados.defineLegend("Sem codificacao")
dados.defineTaxa(1, 1)



for j in range(1,5):
    for i in [5,4.5,4,3.5,3,2.5,2,1.5,1]:
        n = i/(10**j)
        dados.adicionaPonto(n, n)

dados.salvarEmArquivo('Dados//semcodificacao.txt')
