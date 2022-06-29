"""Leia um valor inteiro correspondente à idade de uma pessoa em dias e
informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo
mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12
meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com
objetivo de testar raciocínio matemático simples."""

x = float(input("Digite sua idade em dias: "))

a = (x/365)
r = (x%365)
m = (r/30)
g = (r%30)
d = (g)


print("{anos:.0f} ano(s)".format(anos=a))
print("{meses:.0f} mes(es)".format(meses=m))
print("{dias:.0f} dia(s)".format(dias=d))


