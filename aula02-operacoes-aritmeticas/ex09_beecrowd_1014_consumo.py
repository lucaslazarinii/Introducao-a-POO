"""Calcule o consumo médio de um automóvel sendo fornecidos a distância total
percorrida (em Km) e o total de combustível gasto (em litros)."""

x = float(input("Digite a distância percorrida: "))
y = float(input("Digite o total de combustível gasto: "))

kml = (x/y)

print("{:.5} km/l".format(kml))



