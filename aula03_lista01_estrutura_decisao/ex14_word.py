#14.	Faça um programa que leia 3 notas de um aluno, calcule sua média e mostre seu conceito final conforme a indicação abaixo:
#Abaixo de 5 			–	Reprovado
#Entre 5 e menor que 7	–	Em recuperação
#Igual ou maior que 7 		–	Aprovado

nota1 = float(input("Qual sua nota na primeira avaliação?"))
nota2 = float(input("Qual sua nota na segunda avaliação?"))
nota3 = float(input("Qual sua nota na terceira avaliação?"))
media = ((nota1+nota2+nota3)/3)
print(f'Sua média foi de: {media:.1f}')
if (media<5):
    print("Você foi reprovado.")
elif (5<=media<7):
    print("Você está de recuperação.")
elif (media>=7):
    print("Você foi aprovado.")
    
