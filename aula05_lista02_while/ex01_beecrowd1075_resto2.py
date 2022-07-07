"""Leia um valor inteiro N. Apresente todos os
números entre 1 e 10000 que divididos por N dão resto igual a 2."""

N = int(input("Digite um número: "))
while (N > 10000 or N < 0):
    N = int(input("Digite um número: "))
for i in range (1, 10001):
    if (N%i) == 2:
        print(i)
        

        
    
        

    



