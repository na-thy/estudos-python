
from datetime import date
data = date.today().year
maior = 0
menor = 0
for c in range (1,8):
    ano = int(input("Digite o ano de nascimento do {}º: ".format(c)))
    idade = data - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("Ao todo tivemos {} maiores de idade.".format(maior))
print("E tivemos {} menores de idade.".format(menor))