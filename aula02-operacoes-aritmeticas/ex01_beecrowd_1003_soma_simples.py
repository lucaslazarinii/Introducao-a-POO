#Leia dois valores inteiros, no caso para variáveis A e B.
#A seguir, calcule a soma entre elas e atribua à variável SOMA.
#A seguir escrever o valor desta variável.

a, b = input("Digite dois valores inteiros: ").split()

a = int(a)
b = int(b)

SOMA = (a+b)

print("SOMA = ", SOMA)