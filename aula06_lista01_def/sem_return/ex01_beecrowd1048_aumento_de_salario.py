"""Leia o salário do funcionário e calcule e mostre o novo salário,
bem como o valor de reajuste ganho e o índice reajustado, em percentual."""
def reajuste(salario):
    if salario <= 400:
        novo_salario = salario*1.15
        rj = novo_salario-salario
        print("Novo salario: {:.2f}".format(novo_salario))
        print("Reajuste ganho: {:.2f}".format(rj))
        print("Em percentual: 15%")
    elif salario <= 800:
        novo_salario = salario*1.12
        rj = novo_salario-salario
        print("Novo salario: {:.2f}".format(novo_salario))
        print("Reajuste ganho: {:.2f}".format(rj))
        print("Em percentual: 12%")
    elif salario <= 1200:
        novo_salario = salario*1.10
        rj = novo_salario-salario
        print("Novo salario: {:.2f}".format(novo_salario))
        print("Reajuste ganho: {:.2f}".format(rj))
        print("Em percentual: 10%")
    elif salario <= 2000:
        novo_salario = salario*1.07
        rj = novo_salario-salario
        print("Novo salario: {:.2f}".format(novo_salario))
        print("Reajuste ganho: {:.2f}".format(rj))
        print("Em percentual: 7%")
    elif salario > 2000:
        novo_salario = salario*1.04
        rj = novo_salario-salario
        print("Novo salario: {:.2f}".format(novo_salario))
        print("Reajuste ganho: {:.2f}".format(rj))
        print("Em percentual: 4%")
   
    
g = float(input("Digite seu salário: "))
nv = reajuste(g)