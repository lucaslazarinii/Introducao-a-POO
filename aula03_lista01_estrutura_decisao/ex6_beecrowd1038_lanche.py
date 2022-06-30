#Com base na tabela abaixo, escreva um programa que leia o código
#de um item e a quantidade deste item.
#A seguir, calcule e mostre o valor da conta a pagar.

c, q = input("Digite 2 valores inteiros: ").split()

if c == '1':
    print("Total R$:", (4*int(q)))
elif c == '2':
    print("Total R$:", (4.5*int(q)))
elif c == '3':
    print("Total R$:", (5*int(q)))
elif c == '4':
    print("Total R$:", (2*int(q)))
elif c == '5':
    print("Total R$:", (1.5*int(q)))
    
    

    