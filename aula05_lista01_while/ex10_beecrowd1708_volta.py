"""No automobilismo é bastante comum que o líder de uma prova, em determinado momento,
ultrapasse o último colocado. O líder, neste momento, está uma volta à frente do último
colocado, que se torna, assim, um retardatário. Neste problema, dados os tempos que o
piloto mais rápido e o piloto mais lento levam para completar uma volta, você deve
determinar em que volta o último colocado se tornará um retardatário, ou seja, s
erá ultrapassado pelo líder. Você deve considerar que, inicialmente, eles estão lado a lado,
na linha de partida do circuito, ambos no início da volta de número 1
(a primeira volta da corrida); e que uma nova volta se inicia sempre depois que o líder
cruza a linha de partida."""
j = 0
v1 = 0
p1, p2 = (float(x) for x in input("Segundos necessários para completar uma volta: ").split())

while p1 <= 0 or p2 <= 0 or p1 > 10000 or p2 > 10000:
    print("---------ERRO---------")
    print("Os dados fornecidos devem estar entre o intervalo (1, 10000)")
    p1, p2 = (float(x) for x in input("Segundos necessários para completar uma volta: ").split())

if (p1 == p2):
    print("O último colocado não se tornará um retardatário.")
elif (p1<p2):
    v = (p2-p1)
    j += 1
    while v1 < p1:
        v1 += v
        j += 1
    
elif (p2<p1):
    v = (p1-p2)
    j += 1 
    while v1 < p1:
        v1 += v
        j += 1
print(j)
    
    
    
