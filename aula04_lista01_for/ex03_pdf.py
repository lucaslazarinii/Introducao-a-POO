"""Uma universidade particular oferece um desconto de 30% na mensalidade do
aluno com melhor nota (média geral). Implemente um programa que após
receber as informações do aluno (nome, nota/média geral, valor mensalidade)
verifique quem é o aluno com melhor nota e calcule o desconto de sua
mensalidade.
Ao final de sua execução, o programa deve mostrar:
- o nome do aluno com melhor nota,
- o valor da mensalidade (sem desconto) e
- o valor da mensalidade com o desconto e 30%;
Considerar 5 alunos (as informações devem ser lidas do teclado)."""

a1, b1, c1, d1, e1 = input("Digite o nome dos alunos: ").split()
a2, b2, c2, d2, e2 = input("Digite suas respectivas notas: ").split()
a3, b3, c3, d3, e3 = input("Digite o respectivo valor da mensalidade: ").split()

a2 = float(a2)
b2 = float(b2)
c2 = float(c2)
d2 = float(d2)
e2 = float(e2)

a3 = float(a3)
b3 = float(b3)
c3 = float(c3)
d3 = float(d3)
e3 = float(e3)

if (a2>b2) and (a2>c2) and (a2>d2) and (a2>e2):
    print("Aluno com melhor nota: ", a1)
    print("Valor da mensalidade (sem desconto) R$: ", a3)
    print("Vaçpr da mensalidade (com desconto) R$: ", (a3*0.7))
    
elif (b2>a2) and (b2>c2) and (b2>d2) and (b2>e2):
    print("Aluno com melhor nota: ", b1)
    print("Valor da mensalidade (sem desconto) R$: ", b3)
    print("Valor da mensalidade (com desconto) R$: ", (b3*0.7))
    
elif (c2>a2) and (c2>b2) and (c2>d2) and (c2>e2):
    print("Aluno com melhor nota: ", c1)
    print("Valor da mensalidade (sem desconto) R$: ", c3)
    print("Valor da mensalidade (com desconto) R$: ", (c3*0.7))
    
elif (d2>a2) and (d2>b2) and (d2>c2) and (d2>e2):
    print("Aluno com melhor nota: ", d1)
    print("Valor da mensalidade (sem desconto) R$: ", d3)
    print("Valor da mensalidade (com desconto) R$: ", (d3*0.7))

elif (e2>a2) and (e2>b2) and (e2>d2) and (e2>c2):
    print("Aluno com melhor nota: ", e1)
    print("Valor da mensalidade (sem desconto) R$: ", e3)
    print("Valor da mensalidade (com desconto) R$: ", (e3*0.7))
    
else:
    print("")
    
    
    
    

