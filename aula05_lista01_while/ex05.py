"""Florianópolis é uma cidade que possui diversas praias.
De forma a melhor orientar os turistas a Secretaria Municipal de Turismo mediu
a distância de cada praia a partir do centro da cidade.
Seu programa deve solicitar que o usuário indique o número de praias que deseja
cadastrar. E para cada praia, indique o nome (string) e a distância do centro
da cidade (int).
A partir destas informações, seu programa deve obter os seguintes dados:
•   qual a praia mais distante do centro da cidade;
•   quantas praias estão entre 15 e 20 km do centro;
•  qual a distância média das praias (arredondado na primeira casa decimal);"""

qntpraia = int(input("Digite a quantidade de praias a cadastrar: "))
praiamaislonge = ""
distanciamax = 0
distanciamedia = 0
rpraia = 0
r = 0

while True:
    praianome = str(input("Digite o nome da praia: "))
    distancia = int(input("Digite a distância da praia para o centro (km): "))
    r += 1
    distanciamedia += distancia/r
    if (distancia > distanciamax):
        praiamaislonge = praianome
        distanciamax = distancia
    if (15 <= distancia <= 20):
        rpraia += 1
    if (r >= qntpraia):
        break
    
print("Praia mais distante:", praiamaislonge)
print("Praias que estão entre 15 e 20 km do centro:", rpraia)
print("Distância média das praias: ", distanciamedia)
    