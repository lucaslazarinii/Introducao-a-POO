"""Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência
de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido
(codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário
informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código
(até que seja válido). O programa será encerrado quando o código informado for o número 4."""


print("1.Álcool")
print("2.Gasolina")
print("3.Diesel")
print("4.Fim")
print("Digite o(s) código(s) do(s) combustível(eis) desejado(s):")

r = 0
a = 0
g = 0
d = 0
f = 0

while f != 4:
    f = int(input(""))
    
    if f == 1:
        a += 1
    elif f == 2:
        g += 1
    elif f == 3:
        d += 1
    else:
        print("Fora da faixa 1 a 4, digite novamente:")
        
print("MUITO OBRIGADO")
print("Alcool:", a)
print("Gasolina:", g)
print("Diesel:", d)


    



