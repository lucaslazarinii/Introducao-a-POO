#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
#Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

#Perimetro = XX.X


#Em caso negativo, calcule a área do trapézio que
#tem A e B como base e C como altura, mostrando a mensagem:


#Area = XX.X

a, b, c = input("Digite suas notas: ").split()

if (float(a)+float(b)>float(c)):
    if (float(a)+float(c)>float(b)):
        if (float(c)+float(b)>float(a)):
            print("Perimetro =", (float(a)+float(b)+float(c)))
        else:
            print("Area =", ((float(a)+float(b))*float(c)/2))
    else:
        print("Area =", ((float(a)+float(b))*float(c)/2))
else:
    print("Area =", ((float(a)+float(b))*float(c)/2))
            
