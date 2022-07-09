"""Vovô João tem uma banca de jornais; ele tem muitos clientes, e
diariamente recebe muito dinheiro, mas também faz muitos pagamentos
para manter o seu estoque de jornais e revistas. Todo dia ele vai ao
banco realizar um depósito ou uma retirada de dinheiro.
Em alguns dias, o saldo de sua conta no banco fica negativo, mas Vovô
João tem um acordo com o banco que garante que ele somente é cobrado se
o saldo for menor do que um valor pré-estabelecido.

Dada a movimentação diária da conta do banco do Vovô João, você deve
escrever um programa que calcule o menor saldo da conta, no período dado."""

dia, saldoinicial = (int(x) for x in input("Digite o número de dias e o saldo da conta: ").split())

saldo_atual = 0
saldo_atual += saldoinicial

for i in range(1, dia+1):
    entrada = int(input("Digite a movimentação da conta: "))
    if saldo_atual <= saldo_atual+entrada:
        recorde = saldo_atual
    saldo_atual += entrada
print(recorde)
