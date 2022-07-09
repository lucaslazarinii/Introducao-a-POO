def checar(d):
    div = 0
    for i in range(2, d):
        if (d % i == 0 or d == 1):
            div += 1

    if(div == 0 and d != 1):
        return True
    else:
        return False

def contagem(a, b):
    cont = 0
    c = a
    for i in range(a, b+1):
        if (checar(c)):
            cont +=1
        c += 1
    return cont

x, y = (int(x) for x in input("Digite um intervalo: ").split())

if (x<y):
    print("Há {g} números primos no intervalo escolhido.".format(g=contagem(x,y)))   

else:
    print("Há {g} números primos no intervalo escolhido.".format(g=contagem(y,x)))