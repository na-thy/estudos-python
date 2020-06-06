lista = []
for c in range(1,6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(c)))
    lista.append(peso)
menor = min(lista)
maior = max(lista)
print("O maior peso foi {:.0f}.".format(maior))
print("O menor peso foi {:.0f}.".format(menor))
    