N = int(input("Digite o número de casas que existem na rua: "))
numeros = []
resultados = []
z = 0
while N < 2 or N > 10**5+1:
    print("\n A quantidade de casas deve estar entre 2 e 10^5. Tente novamente.")
    N = int(input("Digite o número de casas que existem na rua: "))
for i in range(N):
    numeros.append(int(input(f"Digite o número da casa {i+1}: ")))
z = int(input("Digite a soma dos números das casas onde estão escondidos os brinquedos: "))
for i in range(len(numeros)):
    for j in range(len(numeros)):
        if numeros[i] != numeros[j] and int(numeros[i])+int(numeros[j]) == z:
            resultados.append(numeros[i])
            resultados.append(numeros[j])
            break
print(resultados[0], resultados[1])  