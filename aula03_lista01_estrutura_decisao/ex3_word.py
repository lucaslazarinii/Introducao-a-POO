#Desenvolva um algoritmo que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com:
#Abaixo de 18,5 – abaixo do peso
#Entre 18.5 e 25 – peso ideal
#Entre 25 e 30 - sobrepeso
#Entre 30 e 40 - obesidade
#Acima de 40 - obesidade mórbida
#Para o cálculo do IMC, considere:  IMC = peso / (altura x altura)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = (peso/(altura*altura))
print ("Seu IMC é: ",(IMC))
if (IMC<18.5):
    print("Você está abaixo do peso!")
elif (18.5<IMC<25):
    print("Você está no peso ideal!")
elif (25<IMC<30):
    print("Você está com sobrepeso!")
elif (30<IMC<40):
    print("Você está com obesidade!")
else:
    print("Você está com obesidade mórbida!")

