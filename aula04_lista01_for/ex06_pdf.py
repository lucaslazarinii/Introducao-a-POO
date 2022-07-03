"""Altere o programa de cálculo dos números primos (exercício 5), informando, caso
o número não seja primo, por qual(is) número(s) ele é divisível."""

x = int(input("Digite um número inteiro: "))

if (x%2) == 0:
    if (x) == 2:
        print ("É número primo")
    else:
        for i1 in range(1, x+1):
            if (x%i1) == 0:
                print("É divisível por:", i1)
elif (x) == 3:
    print ("É número primo")
elif (x%3) == 0:
    for i1 in range(1, x+1):
        if (x%i1) == 0:
            print("É divisível por:", i1)
else:
    print ("É número primo")
    




    