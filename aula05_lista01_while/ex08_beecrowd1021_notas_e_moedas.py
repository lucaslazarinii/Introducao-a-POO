"""Leia um valor de ponto flutuante com duas casas decimais.
Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o
valor pode ser decomposto. As notas consideradas
são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de
1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias."""

N = float(input("Digite um valor: "))
while N >= 1000000.00 or N <= 0:
    N = float(input("Digite um valor entre o invervalo (0 ≤ N ≤ 1000000): "))
    
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
m1 = 0
m050 = 0
m025 = 0
m010 = 0
m005 = 0
m001 = 0

#NOTAS:
while N > 0:
    if (N>=100):
        n100 = N//100
        N -= n100*100
    elif (N>=50):
        n50 = N//50
        N -= n50*50
    elif (N>=20):
        n20 = N//20
        N -= n20*20
    elif (N>=10):
        n10 = N//10
        N -= n10*10
    elif (N>=5):
        n5 = N//5
        N -= n5*5
    elif (N>=2):
        n2 = N//2
        N -= n2*2
#MOEDAS:
    elif (N>=1):
        m1 = N//1
        N -= m1*1
    elif (N>=0.50):
        m050 = N//0.50
        N -= m050*0.50
    elif (N>=0.25):
        m025 = N//0.25
        N -= m025*0.25
    elif (N>=0.10):
        m010 = N//0.10
        N -= m010*0.10
    elif (N>=0.05):
        m005 = N//0.05
        N -= m005*0.05
    elif (N>=0.01):
        m001= N//0.01
        N -= m1*0.01
    else:
        break
        
print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00".format(n100))
print("{:.0f} nota(s) de R$ 50.00".format(n50))
print("{:.0f} nota(s) de R$ 20.00".format(n20))
print("{:.0f} nota(s) de R$ 10.00".format(n10))
print("{:.0f} nota(s) de R$ 5.00".format(n5))
print("{:.0f} nota(s) de R$ 2.00".format(n2))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00".format(m1))
print("{:.0f} moeda(s) de R$ 0.50".format(m050))
print("{:.0f} moeda(s) de R$ 0.25".format(m025))
print("{:.0f} moeda(s) de R$ 0.10".format(m010))
print("{:.0f} moeda(s) de R$ 0.05".format(m005))
print("{:.0f} moeda(s) de R$ 0.01".format(m001))





    



    
