def checagem(nmr):
    p = 0
    for num in range(2, nmr + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               p = num
    return p

def resposta(a, b):
    r = (checagem(a)*checagem(b))
    return r

N, M = (int(x) for x in input("Digite os números escolhidos: ").split())
print(resposta(N, M))



