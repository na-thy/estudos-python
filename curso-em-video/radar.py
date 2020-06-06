velocidade = int(input("Qual a velocidade do carro? "))
multa = (velocidade - 80) * 7.00

if velocidade > 80:
    print("MULTADO: A velocidade permitida é de 80km/h \nVocê deverá pagar uma multa de R${:.2f}".format(multa))
    print("Dirija com segurança.")
else:
    print("Boa viagem!")