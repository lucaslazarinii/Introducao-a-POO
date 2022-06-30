#Elabore um programa que calcule o valor a ser pago por um produto,
#seu programa deve perguntar o valor do produto e a condição de pagamento.
#Considere:
#à vista (dinheiro ou cheque)    – 	10% de desconto
#1x no cartão 			   –	 5% de desconto
#2x cartão			   –	 preço normal
#3x ou mais no cartão 		   -	20% de juros

valor = int(input("Qual o valor do produto? "))
print("Digite o número correspondente a opção de pagamento desejada.")
print("1 - à vista (dinheiro ou cheque)    – 	10% de desconto")
print("2 - 1x no cartão 	     –	 5% de desconto")
print("3 - 2x cartão			           –	 preço normal")
print("4 - #3x ou mais no cartão 		   -	20% de juros")
opcao = input(' ')

if opcao == '1':
    forma1 = input("Dinheiro ou cheque?")
    print("Valor a ser pago: ", (valor*0.9))
elif opcao == '2':
    print("Valor a ser pago: ", (valor*0.95))
elif opcao == '3':
    print("Valor a ser pago: ", (valor))
elif opcao == '4':
    print("Valor a ser pago: ", (valor*1.20))
else:
    print("Erro! Escolha uma forma de pagamento.")

    
    




     








