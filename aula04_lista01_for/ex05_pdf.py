"""Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele
mesmo e por 1."""

x = int(input("Digite um número inteiro: "))

if (x%2) == 0:
    if (x) == 2:
        print ("É número primo")
    else:
        print ("Não é número primo")
elif (x) == 3:
    print ("É número primo")
elif (x%3) == 0:
    print ("Não número primo")
else:
    print ("É número primo")
    
    
    

    
