#Leia 2 valores inteiros (A e B).
#Após, o programa deve mostrar uma mensagem "Sao Multiplos"
#ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

a, b = input("Digite dois valores: ").split()

a = float(a)
b = float (b)

if (a==b):
    print("São múltiplos")
if (a>b):
    if (a%b==0):
        print("São múltiplos")
    else:
        print("Não são múltiplos")
if (b>a):
    if (b%a==0):
        print("São múltiplos")
    else:
        print("Não são múltiplos")
        
    
    
    
    