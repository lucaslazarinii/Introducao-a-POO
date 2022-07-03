"""Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles. No final mostre a soma dos
números (do intervalo)."""

x, y = map(int, input("Digite dois números inteiros diferentes: ").split())

import math

if (x>y):
    print("Intervalo:")
    for i in range(y+1,x):
        print(i)
    print("Soma:", sum(range ((y+1), x, 1)))
        
elif (y>x):
    print("Intervalo:")
    for i in range(x+1,y):
        print(i)
    print("Soma:", sum(range((x+1), y, 1)))
        
elif (x==y):
    print("Digite números diferentes.")
    
        
