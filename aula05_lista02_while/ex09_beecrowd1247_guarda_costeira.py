""""Pega ladrão! Pega ladrão!" Roubaram a bolsa de uma inocente senhora que caminhava na praia da Nlogônia e o
ladrão fugiu em direção ao mar. Seu plano parece obvio: ele pretende pegar um barco e escapar!

O fugitivo, que a essa altura já está a bordo de sua embarcação de fuga, pretende seguir
perpendicularmente à costa em direção ao limite de aguas internacionais, que fica a 12 milhas
náuticas de distância, onde estará são e salvo das autoridades locais.
Seu barco consegue percorrer essa distância a uma velocidade constante de VF nós.

A Guarda Costeira pretende interceptá-lo, e sua embarcacão tem uma velocidade constante de VG
nós. Supondo que ambas as embarcações partam da costa exatamente no mesmo instante, com uma
distância de D milhas náuticas entre elas, será possível aGuarda Costeira alcançar
o ladrão antes do limite de aguas internacionais?

Assuma que a costa da Nlogônia é perfeitamente retilínea e o mar bastante calmo,
de forma a permitir uma trajetória tão retilínea quanto a costa."""

D, VF, VG = (float(x) for x in input("Digite a VF, VG e a distância entre os barcos: ").split())

while VF < 1 or VG < 1 or D < 1 or VF > 100 or VG >100 or D > 100:
    print("---------ERRO---------")
    print("Os números devem estar entre o intervalo (1, 100)")
    VF, VG, D = (float(x) for x in input("Digite a distância entre os barcos, VF e VG: ").split())
from math import sqrt
VF = 12/VF
VG = ((sqrt(12**2+D**2))/VG)
if (VG>VF):
    print("N")
else:
    print("S")
    
    


    



