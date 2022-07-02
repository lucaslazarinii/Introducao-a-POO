"""Estamos no ano 2048 e um dos sonhos da humanidade torna-se finalmente realidade:
a colonização do planeta Marte. Nossos primeiros colonizadores acabam de chegar,
e já começam a fazer as preparações (como a instalação de cúpulas de oxigênio
e tratamento do solo para agricultura) para que mais pessoas possam tentar
uma nova vida no planeta vizinho.

Apesar dos avanços tecnológicos e desafios vencidos, ainda resta um
grande problema: os foguetes usados para ir a Marte ainda são complicados e caros.
Com isso, fica difícil enviar suprimentos para os nossos colonos
(enquanto a agricultura ainda não é possível) por muito tempo.
Assim, a agência espacial contratou o SBC (Serviço Balístico Cósmico),
que desenvolveu um canhão super-potente que consegue disparar esferas até
Marte, sem precisar gastar milhões de dólares em equipamento e combustível.

Agora, tudo o que é necessário fazer para enviar suprimentos a Marte é
colocar uma caixa com as encomendas dentro de uma esfera e disparar a
mesma até seu destino.

Dadas as dimensões de uma caixa com suprimentos e o raio interno da
esfera que é disparada pelo canhão, seu programa deverá dizer se é
possível enviar tal caixa para Marte usando tal esfera."""

L, A, P, R = input("Digite quatro números inteiros: ").split()

#largura
#altura
#profundidade
#raio

L = float(L)
A = float (A)
P = float (P)
R = float (R)


#metade diagonal do quadrado:
import math
d= ((math.sqrt(2)*L)/2)

if (R>=d):
    print ("S")
else:
    print("N")

