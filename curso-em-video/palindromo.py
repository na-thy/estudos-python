frase = str(input("Digite sua frase: ")).strip().lower()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print("O inverso de {} é {}.".format(frase,inverso))
if inverso == junto:
    print("É UM PALÍNDROMO")
else:
    print("NÃO É PALÍNDROMO")
