r = "S"
soma_idades = 0
soma_pessoas = 0
sexo_feminino = 0
idade = 0
maior_idade = 0
sexo_menor = ""
idade_menor = 0
pessoa_velha = ""
def idade_media(x, y):
    media= x/y
    print()
    print("Idade média do grupo: {:.1f}".format(media))
    print("Quantidade de mulheres com salário maior que R$2000:", sexo_feminino)
    print("Morador com menor salário possui", idade_menor, "anos e pertence ao sexo", sexo_menor)
    print("Morador mais velho:", pessoa_velha)

    
while r == "S":
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo: [M/F] ").upper())
    salario = float(input("Digite seu salário: "))
    menor_salario = salario
    if sexo == "F":
        if salario > 2000:
            sexo_feminino += 1
    if salario <= menor_salario:
        salario = menor_salario
        sexo_menor = sexo
        idade_menor = idade
    soma_idades += idade
    soma_pessoas += 1
    if maior_idade < idade:
        maior_idade = idade
        pessoa_velha = nome
    r = str(input("Deseja continuar cadastrando? [S/N]").upper())
    print()
        
idade_media(soma_idades, soma_pessoas)

        

    
    
    
    