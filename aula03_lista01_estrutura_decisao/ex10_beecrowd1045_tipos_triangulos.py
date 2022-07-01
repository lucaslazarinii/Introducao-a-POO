"""Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente,
de modo que o lado A representa o maior dos 3 lados. A seguir,
determine o tipo de triângulo que estes três lados formam, com base
nos seguintes casos, sempre escrevendo uma mensagem adequada:"""

primeiro, segundo, terceiro = input("Digite três valores: ").split()

primeiro = float(primeiro)
segundo = float(segundo)
terceiro = float(terceiro)
a = float(1)
b = float(1)
c = float(1)

if (primeiro>=segundo) and (primeiro>=terceiro): #a>
    a = primeiro
    if (segundo>=terceiro): #a>b>c
        b = segundo
        c = terceiro
    else:                   #a>c>b
        c = segundo
        b = terceiro
        
if (segundo>=primeiro) and (segundo>=terceiro): #a>
    a = segundo
    if (primeiro>=terceiro):                    #a>b>c
        b = primeiro
        c = terceiro
    else:                  #a>c>b
        b = terceiro
        c = primeiro
        
if (terceiro>=primeiro) and (terceiro>=segundo): #a>
    a = terceiro
    if (primeiro>=segundo):                    #a>b>c
        b = primeiro
        c = segundo
    else:                       #a>c>b
        b = segundo
        c = primeiro
if (primeiro==segundo==terceiro):
    a = primeiro
    b = segundo
    c = terceiro
    print("TRIÂNGULO EQULÁTERO")
if (a>=(b+c)):
    print("NÃO FORMA TRIÂNGULO")
else:
    if ((a**2) == (b**2) + (c**2)):
        print("TRIÂNGULO RETÂNGULO")
    if ((a**2) > (b**2) + (c**2)):
        print("TRIÂNGULO OBTUSÂNGULO")
    if ((a**2) < (b**2) + (c**2)):
        print("TRIÂNGULO ACUTÂNGULO")
    if (a==b !=c or b==c !=a or a==c !=b):
        print("TRIÂNGULO ISÓSCELES")
        
        
    
    
    
    
    
    


        
    
    

    
        
            
            
            
            
            
            
            
            
            
            
            
                
           
            