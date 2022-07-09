E1 = set(input("Digite os clientes da empresa um: ").split())
E2 = set(input("Digite os clientes da empresa dois: ").split())

print(f"\n\nQuantidade de clientes cadastrados na empresa 1: {len(E1)}")
print(f"Quantidade de clientes cadastrados na empresa 2: {len(E2)}")

while True:
    r1 = input("\nDeseja cadastrar um novo cliente? [S/N] ").upper()
    if r1 == "S":
        r2 = int(input("Em qual empresa deseja realizar o cadastro? [1/2] "))
        while r2 > 2 or r2 < 0:
            print("\nSomente são aceitos os valores 1 e 2. Tente novamente.")
            r2 = int(input("Em qual empresa deseja realizar o cadastro? [1/2] "))
        if r2 == 1:
            E1.add(input("Digite o nome do cliente: "))
        else:
            E2.add(input("Digite o nome do cliente: "))
        True
    elif r1 == "N":
        break
    else:
        print("\nÉ necessário responder 'S' ou 'N'")
        True

print(f"\n\nQuantidade de clientes cadastrados na empresa 1: {len(E1)}")
print(f"Quantidade de clientes cadastrados na empresa 2: {len(E2)}")
print(f"Clientes cadastrados nas duas empresas: {E1.intersection(E2)}")
print(f"Clientes cadastrados em somente uma empresa: {E1.symmetric_difference(E2)}")
print(f"Total de clientes: {len(E1.symmetric_difference(E2))+len(E1.intersection(E2))}")