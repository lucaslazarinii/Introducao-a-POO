def verificar():
    impar = 0
    par = 0
    for i in range(1, 11):
        y = float(input("Digite um número a ser verificado: "))
        if y%2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar
par, impar = verificar()

print("Números pares: {}".format(par))
print("Números ímpares {}".format(impar))





