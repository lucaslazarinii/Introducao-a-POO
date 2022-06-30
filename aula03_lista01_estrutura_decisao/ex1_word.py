"""Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado"""

valor = float(input("Digite valor da casa:  "))
salario =float(input("Digite seu salário: "))
tempo = int(input("Digite em anos quanto tempo irá pagar: "))
prestacao = valor/(tempo*12)

if (prestacao > (salario*0.3) ):
    print("Empréstimo negado")
    
else:
    print("Empréstimo aprovado")
    print ("O valor da prestação é: {:.2f} ".format(prestacao))
    