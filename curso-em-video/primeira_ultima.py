frase = str(input("Digite uma frase: ")).strip().upper()

a = frase.find("A")+1
b = frase.count("A")
c = frase.rfind("A")+1

print("A letra A aparece {} vezes na frase.".format(b))
print("A primeira letra A aparece na posição {}.".format(a))
print("A última letra A aparece na posição {}.".format(c))