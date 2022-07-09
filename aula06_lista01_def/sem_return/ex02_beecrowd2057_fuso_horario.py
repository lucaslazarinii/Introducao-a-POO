"""Paulo e Pedro fizeram uma longa jornada desde que partiram do Brasil
para competir na Final Mundial da Maratona, em Phuket, Tailândia. Notaram
que a cada escala que faziam, tinham que ajustar seus relógios por causa do
fuso horário.

Assim, para melhor se organizarem para as próximas viagens, eles pediram
que você faça um aplicativo para celular que, dada a hora de saída, tempo de
viagem e o fuso do destino com relação à origem, você informe a hora de chegada
de cada vôo no destino.

Por exemplo, se eles partiram às 10 horas da manhã para uma viagem de 4 horas
rumo a um destino que fica à leste, em um fuso horário com uma hora a mais com
relação ao fuso horário do ponto de partida, a hora de chegada terá que ser: 10
horas + 4 horas de viagem + 1 hora de deslocamento pelo fuso, ou seja, chegarão
às 15 horas. Note que se a hora calculada for igual a 24, seu programa deverá
imprimir 0 (zero)."""

def chegada(S, T, F):
    hrchegada = S+T+F
    if hrchegada >= 24:
        g = hrchegada - 24
        print(g)
    elif hrchegada == 0:
        print("00")
    elif hrchegada < 0:
        print(24+hrchegada)    
    else:
        print(hrchegada)
S, T, F = (int(x) for x in input("Digite a hora da saida, tempo de viagem e o fuso horário: ").split())
chegada(S, T, F)
    