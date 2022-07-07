"""Vó Vitória mantém, desde o nascimento dos netos Joãozinho e Zezinho, um ritual que faz a
alegria dos meninos. Ela guarda todas as moedas recebidas como troco em dois pequenos
cofrinhos, um para cada neto. Quando um dos cofrinhos fica cheio, ela chama os dois netos
para um alegre almoço, ao final do qual entrega aos garotos as moedas guardadas nos
cofrinhos de cada um.

Ela sempre foi muito zelosa quanto à distribuição igualitária do troco arrecadado.
Quando, por força do valor das moedas, ela não consegue depositar a mesma quantia nos
dois cofrinhos, ela memoriza a diferença de forma a compensá-la no próximo depósito.

Vó Vitória está ficando velha e tem medo que deslizes de memória a façam cometer
injustiças com os netos, deixando de compensar as diferenças entre os cofrinhos.
Sua tarefa é ajudar Vó Vitória, escrevendo um programa de computador que indique as
diferenças entre os depósitos, de forma que ela não tenha que preocupar-se em memorizá-las."""

t = 1
x = 0
while x == 0:
    x = int(input("Digite a quantidade de depósitos: "))
    while x < 0 or x > 100:
            print("")
            print("Quantidade de depósitos deve ser um valor entre 1 e 100.")
            x = int(input("Digite a quantidade de depósitos: "))    
while x != 0:
    print("Teste", t)
    d = 0
    while x >= 1:
        J, Z = (int(x) for x in input("Digite os valores a serem depositados (em centavos): ").split())        
        if (J > Z):
            d += (J-Z)
            x += -1
            print("Diferença atual: ", d)
        elif (J < Z):
            d += (J-Z)
            x += -1
            print("Diferença atual: ", d)
        else:
            x += -1
            print("Diferença atual: ", d)
    x = int(input("Digite a quantidade de depósitos: "))
    t += 1


    


    
        
