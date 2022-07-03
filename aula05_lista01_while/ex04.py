"""Implementar um programa que calcula o desconto previdenciário dos funcionários
de uma empresa.
O algoritmo deve, dado um salário, retornar o valor do desconto proporcional ao
mesmo."""

"""- O cálculo de desconto segue a seguinte regra: o desconto deve ser de 11% do
valor do salário, entretanto, o valor máximo de desconto é R$320,00.
Sendo assim, seu programa deve verificar se calculará sobre 11%  do salário ou
utilizará o teto R$320,00. No caso, de o desconto aplicado for R$320,00,
seu programa deve indicar qual foi o % de desconto aplicado para este funcionário.	
- Critério de parada definido pelo usuário (perguntar a cada
verificação se deseja continuar)"""

r = 'S'
s = 0

while r == 'S':
    s = float(input("Insira seu salário: "))
    if (s>=2909):
        print("Desconto máximo atingido (11%).")
        print("Desconto aplicado: R$320.00")
    else:
        d = s*0.11
        print("Desconto aplicado: R${:.2f}".format(d))
        
    r = str(input("Deseja continuar? [S/N]"))
    


