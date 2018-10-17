def geraVetorRec(result, palavra, tamanho):
    if tamanho == 0:
        result.append(palavra[:])
    else:
        palavra[-tamanho] = 0
        geraVetorRec(result, palavra, tamanho-1)
        palavra[-tamanho] = 1
        geraVetorRec(result, palavra, tamanho-1)

def geraVetor(tamanho_da_palavra):
    info = []
    palavra = [0]*tamanho_da_palavra
    geraVetorRec(info, palavra, tamanho_da_palavra)
    return info[:]

    