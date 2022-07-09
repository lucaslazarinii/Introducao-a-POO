r, c = (int(x) for x in input("Digite a quantidade de leituras e a capacidade máxima do elevador: ").split())
pessoas = 0
resultado = "N"
for i in range (1, r+1):
    s, e = (int(x) for x in input("Digite quantas pessoas saíram e quantas entraram: ").split())
    pessoas -= s
    pessoas += e
    if pessoas > c:
        resultado = "S"
print(resultado)
    