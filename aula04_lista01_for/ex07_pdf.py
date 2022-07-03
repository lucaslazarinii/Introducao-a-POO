"""Faça um programa que peça para n pessoas a sua idade (o valor de n será
solicitado ao usuário), ao final o programa deverá verificar se a média de idade
da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é
jovem, adulta ou idosa, conforme a média calculada."""


n = int(input("Digite a quantidade de pessoas: "))
s = 0
for i in range (1, n+1):
    x = int(input("Digite a idade: "))
    s += x
m = s/n
if (0<=m<=25):
    print("Turma jovem.")
elif (25<=m<=60):
    print("Turma adulta.")
elif (m>60):
    print ("Turma idosa.")
        

    
 
    
    