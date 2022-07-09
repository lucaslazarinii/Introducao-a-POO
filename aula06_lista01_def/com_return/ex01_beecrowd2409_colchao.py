"""João está comprando móveis novos para sua casa. Agora é a vez de
comprar um colchão novo, de molas, para substituir o colchão velho.
As portas de sua casa têm altura H e largura L e existe um colchão que
está em promoção com dimensões A × B × C.

O colchão tem a forma de um paralelepípedo reto retângulo e João
só consegue arrastá-lo através de uma porta com uma de suas faces
paralelas ao chão, mas consegue virar e rotacionar o colchão antes de
passar pela porta.

Entretanto, de nada adianta ele comprar o colchão se ele não
passar através das portas de sua casa. Portanto ele quer saber
se consegue passar o colchão pelas portas e para isso precisa de sua
ajuda."""
def calculo(ac, lc, cc, ap, lp):
    if (ac <= ap and lc <= lp):
        resultado = "S"
    elif (ac <= ap and cc <= lp):
        resultado = "S"
    elif (lc <= ap and ac <= lp):
        resultado = "S"
    elif (lc <= ap and cc <= lp):
        resultado = "S"
    elif (cc <= ap and ac <= lp):
        resultado = "S"
    elif (cc <= ap and lc <= lp):
        resultado = "S"
    else:
        resultado = "N"
    return resultado

A, B, C = (int(x) for x in input("Digite as três dimensões do colchão (cm): ").split())
while A < 1 or B < 1 or C < 1 or A > 300 or B > 300 or C > 300:
    print()
    print("Dados inseridos incorretamente, respeite o seguinte intervalo:")
    print("(1 ≤ A, B, C ≤ 300)")
    A, B, C = (int(x) for x in input("Digite as três dimensões do colchão (cm) novamente: ").split())
H, L = (int(x) for x in input("Digite a altura e largura das portas (cm): ").split())
while H < 1 or L < 1 or H > 250 or L > 250:
    print()
    print("Dados inseridos incorretamente, respeite o seguinte intervalo:")
    print("(1 ≤ H, L ≤ 250)")
    H, L = (int(x) for x in input("Digite a altura e largura das portas (cm) novamente: ").split())

salario = calculo(A, B, C, H, L)
print(salario)