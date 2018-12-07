# gera os valores de p com base no Ei/N0(dB) e R desejados

import math

def pfromEiN0(ein0, rate):
    return 1/2*math.exp(-rate*pow(10,ein0/10))

eino = []
inicio = 0
passo = 0.5
max = 10
while inicio <= max:
    eino.append(inicio)
    inicio += passo

p = []
for i in eino:
    p.append(pfromEiN0(i,1/1))

print(p)