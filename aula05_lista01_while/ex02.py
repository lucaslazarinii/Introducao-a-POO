""" Implemente um jogo onde o usuário deve adivinhar o número escolhido
pelo computador (entre 0 e 10). O Usuário irá digitando valores até descobrir
este valor. Quando o usuário “acertar”, uma mensagem avisa o final do jogo
(que o número correto foi digitado) e o número de tentativas"""

from random import randrange

x = randrange(11)
y = 12
t = 0

while y != x:
    y = int(input("Digite um número: "))
    t += 1
else:
    print("Você acertou!")
    print("O número secreto era:", x)
    print("Tentativas:", t)
    
