positivo = 0
negativo = 0
Q = int(input("Digite a quantidade de pessoas que participaram da pesquisa: "))
while Q < 4 or Q > 233000:
    print("\nA quantidade de pessoas deve estar entre 4 e 233000. Tente novamente.")
    Q = int(input("Digite a quantidade de pessoas que participaram da pesquisa: "))
resultado = list(input("Digite o resultado: ").split())
while len(resultado) != Q:
    print("\nA quantidade de resultados não corresponde com a quantidade de participantes. ")
    resultado = list(input("Digite o resultado novamente: ").split())
for i in range(Q):
    if int(resultado[i]) == 1:
        negativo += 1
    elif int(resultado[i]) == 0:
        positivo += 1
    else:
        while True:
            print()
            print(int(resultado[i]), "não pode ser lido. Somente são aceitos 0 e 1.\nTente novamente.")
            resultado[i] = int(input("Digite este resultado novamente: "))
            if int(resultado[i]) == 1:
                negativo += 1
                break
            elif int(resultado[i]) == 0:
                positivo += 1
                break
            else:
                True
if negativo >= positivo:
    print("N")
else:
    print("Y")

            
    
