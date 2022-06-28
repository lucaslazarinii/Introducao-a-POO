"""Leia dois valores inteiros.
A seguir, calcule o produto entre estes dois valores e atribua
esta operação à variável PROD.
A seguir mostre a variável PROD com mensagem correspondente.  """

a, b = input("Digite dois valores inteiros: ").split()

a = int(a)
b = int(b)

PROD = (a*b)

print("PROD = ", PROD)