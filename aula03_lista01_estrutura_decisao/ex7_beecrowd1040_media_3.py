"""Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal,
correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas
notas e mostre esta média acompanhada pela mensagem "Media: ".
Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.".
Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa
deve imprimir a mensagem "Aluno em exame.".
No caso do aluno estar em exame, leia um valor correspondente à nota
do exame obtida pelo aluno.
Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2).
e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais )
ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos).
Para estes dois casos (aprovado ou reprovado após ter pego exame)
apresente na última linha uma mensagem "Media final: "
seguido da média final para esse aluno."""

a, b, c, d = input("Digite suas notas: ").split()

media = (((float(a)*2)+(float(b)*3)+(float(c)*4)+(float(d)*1))/10)

if (media>=7):
    print("Média: {:.1f}".format(media))
    print("Aluno aprovado.")
elif (media<5):
    print("Média: {:.1f}".format(media))
    print("Aluno reprovado.")
elif (5<=media<7):
    print("Média: {:.1f}".format(media))
    print("Aluno em exame.")
    exame = input("Nota do exame: ")
    mediaexame = ((float(media)+float(exame))/2)
    if (mediaexame>=5):
        print("Aluno aprovado.")
        print("Média final: {:.1f}".format(mediaexame))
    else:
        print("Aluno reprovado.")
    
else:
    print("Dados incorretos")
    



