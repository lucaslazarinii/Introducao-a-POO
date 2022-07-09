N = int(input("Digite a quantidade de testes:"))
l = []
while N < 0:
    print("A quantidade de testes deve ser um valor positivo.")
    N = int(input("Digite a quantidade de testes novamente:"))
for i in range(0, N):
    l.clear()
    C, R = (int(x) for x in input("Digite a quantidade de chutes feitos pelos alunos e a resposta correta:"))
    l.append(int(input("Digite os chutes:").split()))
    while len(l) != C:
        l.clear()
        print("\n\nA quantidade de chutes não corresponde com os parametrôs inseridos previamente.")
        l.append(int(input("Digite os chutes:").split()))
    x = 1
    r = 0
    while True:
        for i in range(0, x):
            y = l.count(R + i)
            z = l.count(R - i)
            if y > 0 or z >0:
                r = i
                break
            else:
                x += 1
    print(i)