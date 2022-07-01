"""Para descontrair os alunos após as provas da OBI, a Diretora da escola organizou
um campeonato de aviões de papel. Cada aluno participante receberá uma certa
quantidade de folhas de um papel especial para fazer os seus modelos de aviões.
A quantidade de folhas que cada aluno deverá receber ainda
não foi determinada: ela será decidida pelos juízes do campeonato.

A diretora convidou, para atuarem como juízes, engenheiros da Embraer,
uma das mais bem sucedidas empresas brasileiras, que vende aviões com
tecnologia brasileira no mundo todo. O campeonato está programado para
começar logo após a prova da OBI, mas os juízes ainda não chegaram à escola.
A diretora está aflita, pois comprou uma boa quantidade de folhas de papel
especial, mas não sabe se a quantidade comprada vai ser suficiente.

Considere, por exemplo, que a Diretora comprou 100 folhas de papel especial,
e que há 33 competidores. Se os juízes decidirem que cada competidor tem
direito a três folhas de papel, a quantidade comprada pela diretora é suficiente.
Mas se os juízes decidirem que cada competidor tem direito a quatro folhas,
a quantidade comprada pela diretora não seria suficiente.

Você deve escrever um programa que, dados o número de competidores,
o número de folhas de papel especial compradas pela Diretora e o número de
folhas que cada competidor deve receber, determine se o número de folhas
comprado pela Diretora é suficiente."""

C, P, F = input("Digite três valores inteiros:").split()

# C = competidores
# P = folhas de papel compradas
# F = folhas de papel por competidor
# X = folhas necessárias

C = float(C)
P = float(P)
F = float(F)

X = (C*F)

if (X>P):
    print("N")
else:
    print("S")
