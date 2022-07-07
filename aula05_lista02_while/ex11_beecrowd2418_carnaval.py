"""O Carnaval é um feriado celebrado normalmente em fevereiro; em muitas cidades brasileiras,
a principal atração são os desfiles de escolas de samba. As várias agremiações desfilam ao som de
seus sambas-enredos e são julgadas pela liga das escolas de samba para
determinar a campeã do Carnaval.

Cada agremiação é avaliada em vários quesitos; em cada quesito, cada escola recebe cinco
notas que variam de 5,0 a 10,0. A nota final da escola em um dado quesito é a soma das
três notas centrais recebidas pela escola, excluindo a maior e a menor das cinco notas.

Como existem muitas escolas de samba e muitos quesitos, o presidente da liga pediu que
você escrevesse um programa que, dadas as notas da agremiação, calcula a sua nota final num
dado quesito."""

l = [float(x) for x in input("Digite as notas: ").split()]
while len(l) < 5 or len(l) > 5:
    print("------------------")
    print("Apenas cinco notas são aceitas.")
    l = [float(x) for x in input("Digite as notas novamente: ").split()]
a = l[0]
b = l[1]
c = l[2]
d = l[3]
e = l[4]
while a < 5 or b < 5 or c < 5 or d < 5 or e < 5 or l[0] > 10 or a > 10 or b >10 or c >10 or d > 10 or e > 10:
    print("------------------")
    print("As novas devem estar valer entre 5 e 10.")
    l = [float(x) for x in input("Digite as notas novamente: ").split()]
    a = l[0]
    b = l[1]
    c = l[2]
    d = l[3]
    e = l[4]
   
maxi = 0
mini= 0

for i in range(0,5):
    if (l[i] > maxi):
        maxi = l[i]
        mini = maxi
for i in range (0,5):
    if (l[i] < mini):
        mini = l[i]

nt = ((a+b+c+d+e) -(maxi+mini))
print("Nota final: {}".format(nt))


    
          



