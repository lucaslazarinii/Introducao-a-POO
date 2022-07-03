"""10) Considerar uma turma da Disciplina de Cálculo I, com 5 alunos, fazer um
programa que:
10.1) Calcule a média das notas;
10.2) Indique o nome do aluno com a média mais alta
10.3) Informe seu conceito (Aprovado, Em Recuperação, Reprovado).
Considerando que essas regras funcionam da mesma forma que na UFSC:
se a média for 5.75 ou maior, o aluno está aprovado, se a nota for maior
ou igual a 2.75, ele tem o direito de fazer a prova de recuperação e se o
aluno obtiver uma média menor que 2.75 ele foi reprovado."""


maxm = 0
maxn = ""
m = 0
s = ""

for i in range(1,6):
    n = input("Digite seu nome: ")
    n1 = int(input("Digite a nota na primeira prova: "))
    n2 = int(input("Digite a nota na segunda prova: "))
    n3 = int(input("Digite a nota na terceira prova: "))
    m = ((n1+n2+n3)/3)
    if (maxm < m):
        maxm = m
        maxn = n
        if (maxm>=5.75):
            s = "Aprovado!"
        elif ( 2.75 <= maxm < 5.75):
            s = "Recuperação!"
        else:
            s = "Reprovado!"
    
print("----------RESULTADOS----------")
print("Aluno com média mais alta:", maxn)
print("Maior média:", maxm)
print("Situação:", s)




    
