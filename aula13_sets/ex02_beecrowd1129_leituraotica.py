q = int(input("Digite a quantidade de questões: "))
while q < 0 or q > 255:
    print("\nA quantidade de questões deve estar entre 1 e 255.")
    q = int(input("Digite a quantidade de questões novamente: "))
for i in range(1, q+1):
    a = 256
    menor = 0
    c = 0
    s = True
    l = list(input(f"Digite o status da questão {i}: ").split())
    while len(l) != 5:
        print("\nDeve ser fornecido exatamente 5 status.")
        l = list(input(f"Digite o status da questão {i}: ").split())
    for j in range(0, 5):
        while int(l[j]) < 0 or int(l[j]) > 255:
            print("\nO status de cada alternativa deve estar entre 1 e 255. Tente novamente. ")
            if j == 0:
                l[j] = int(input("Digite novamente o status da alternativa A: "))
            elif j == 1:
                l[j] = int(input("Digite novamente o status da alternativa B: "))
            elif j == 2:
                l[j] = int(input("Digite novamente o status da alternativa C: "))
            elif j == 3:
                l[j] = int(input("Digite novamente o status da alternativa D: "))
            elif j == 4:
                l[j] = int(input("Digite novamente o status da alternativa E: "))
        if int(l[j]) <= 127:
            if l.count(l[j]) > 1:
                s = False
            else:
                s = True           
        if int(l[j]) <= a:
            a = int(l[j])
            menor = j
    if s == True:
        if menor == 0:
            print("A")
        elif menor == 1:
            print("B")
        elif menor == 1:
            print("C")
        elif menor == 1:
            print("D")
        elif menor == 1:
            print("E")
    else:
        print("*")
        
            
            
    
    
        
    