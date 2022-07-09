somasala = 0
resultado = ""
aluno = 0
sala = 0
def medias(aluno, sala):
    somamedias = 0
    for i in range(1, 6):
        n1, n2, n3 = (float(x) for x in (input("Digite as notas do aluno {}: ".format(i)).split()))
        while n1 > 10 or n2 > 10 or n3 > 10 or n1 < 0 or n2 < 0 or n3 < 0:
                print()
                print("A nota deve estar entre 0 e 10.")
                n1, n2, n3 = (float(x) for x in (input("Digite as notas do aluno {}: ".format(i)).split()))
        media = ((n1+n2+n3)/3)
        somamedias += media
        sala = somamedias/5
        if media > aluno:
            aluno = media
        
    return aluno, sala
def situacao(aluno, resultado):
    if aluno >= 5.75:
        resultado = "Aprovado!"
    if 2.75 <= aluno < 5.75:
        resultado = "Recuperação!"
    if aluno < 2.75:
        resultado = "Reprovado!"
    return resultado
situacao = situacao(aluno, resultado)
aluno, sala = medias(aluno, sala)

print("A média da turma foi de: {s:.1f}".format(s = sala))
print("O aluno com maior média foi {}".format(situacao))


        
        
        
    
        