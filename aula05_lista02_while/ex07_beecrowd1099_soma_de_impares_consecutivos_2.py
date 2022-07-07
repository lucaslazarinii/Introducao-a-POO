"""Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste de dois inteiros X e Y.
Você deve apresentar a soma de todos os ímpares existentes entre X e Y."""

t = int(input("Digite a quantidade de testes desejada: "))
r = 0
g = 0

while g < t:
        x1, x2 = (int(x) for x in input("Digite dois o intervalo:").split())
        if (x1>x2):
            for i in range(x2+1, x1):
                if (i%2 != 0):
                    r += i
                else:
                    r += 0
        elif (x2>x1):
            for i in range(x1+1, x2):
                if (i%2 != 0):
                    r += i
                else:
                    r += 0
        g += 1
print(r)
                
    



