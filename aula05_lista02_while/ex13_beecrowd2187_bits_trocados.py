"""As Ilhas Weblands formam um reino independente nos mares do Pacífico.
Como é um reino recente, a sociedade é muito influenciada pela informática.
A moeda oficial é o Bit; existem notas de B$ 50,00, B$10,00, B$5,00 e B$1,00.
Você foi contratado(a) para ajudar na programação dos caixas automáticos de um g
rande banco das Ilhas Weblands.

Os caixas eletrônicos das Ilhas Weblands operam com todos os tipos de notas
disponíveis, mantendo um estoque de cédulas para cada valor (B$ 50,00, B$10,00,
B$5,00 e B$1,00). Os clientes do banco utilizam os caixas eletrônicos para
efetuar retiradas de um certo número inteiro de Bits. 

Sua tarefa é escrever um programa que, dado o valor de Bits desejado pelo cliente,
determine o número de cada uma das notas necessário para totalizar esse valor,
de modo a minimizar a quantidade de cédulas entregues. Por exemplo, se o cliente
deseja retirar B$50,00, basta entregar uma única nota de cinquenta Bits.
Se o cliente deseja retirar B$72,00, é necessário entregar uma nota de B$50,00,
duas de B$10,00 e duas de B$1,00.

"""
n50 = 0
n10 = 0
n5 = 0
n1 = 0
t = 0
V = int(input("Digite o valor a ser sacado: "))
while V > 10000:
    print("")
    print("Valor a ser sacado deve ser menor ou igual a 10000.")
    V = int(input("Digite o valor a ser sacado: "))
while V < 0:
    print("")
    print("Valor a ser sacado deve ser maior ou igual a 0.")
    V = int(input("Digite o valor a ser sacado: "))    
while V > 0:
    while V//50 != 0:
        n50 += 1
        V -= 50
    while V//10 != 0:
        n10 += 1
        V -= 10
    while V//5 != 0:
        n5 += 1
        V -= 5
    while V//1 != 0:
        n1 += 1
        V -= 1
    t += 1
    print("Teste", t)
    print (n50, n10, n5, n1)
    n50 = 0
    n10 = 0
    n5 = 0
    n1 = 0
    V = int(input("Digite o valor a ser sacado: "))

    
    



