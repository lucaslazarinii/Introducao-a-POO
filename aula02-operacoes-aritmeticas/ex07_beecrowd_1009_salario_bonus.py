"""Faça um programa que leia o nome de um vendedor,
o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
informar o total a receber no final do mês, com duas casas decimais."""

vendedor = input("Insira nome do vendedor: ")
salario = input("Insira seu salário fixo: ")
vendas = input("Total de vendas em dinheiro efetuadas no mês: ")

salario = float(salario)
vendas = float(vendas)

total = (salario+(vendas*0.15))

print("TOTAL = R$ {:.2f}".format(total))