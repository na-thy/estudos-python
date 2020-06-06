numero = int(input("Me diga um número: "))

resultado = numero % 2
if resultado == 0:
    print("O número {:.0f}".format(numero),"é PAR")

else:
    print ("O número {:.0f}".format(numero), "é ÍMPAR")

