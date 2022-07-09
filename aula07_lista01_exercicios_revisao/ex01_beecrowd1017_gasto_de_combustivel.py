"""Joaozinho quer calcular e mostrar a quantidade de litros de
combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L.
Para isso, ele gostaria que você o auxiliasse através de um simples programa.
Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas)
e a velocidade média durante a mesma (em km/h). Assim, pode-se obter
distância percorrida e, em seguida, calcular quantos litros seriam necessários.
Mostre o valor com 3 casas decimais após o ponto."""

t = int(input("Digite o tempo em horas gasto na viagem: "))
v = int(input("Digite a velocidade média durante a viagem (km/h): "))

d = t*v
l = d/12

print("Quantidade de litros necessária para realizar a viagem: {:.3f}".format(l))
