peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)

if imc <= 18.5:
    print("O IMC dessa pessoa é de {:.1f}".format(imc))
    print("Você está abaixo do peso normal.")
elif 18.5 <= imc < 25:
    print("O IMC dessa pessoa é de {:.1f}".format(imc))
    print("Você está no peso ideal.")
elif 25 <= imc < 30:
    print("O IMC dessa pessoa é de {:.1f}".format(imc))
    print("Você está com sobrepeso.")
elif 30 <= imc < 40:
    print("O IMC dessa pessoa é de {:.1f}".format(imc))
    print("Você está com obesidade.")
else:
    print("O IMC dessa pessoa é de {:.1f}".format(imc))
    print("Você está com obesidade mórbida.")