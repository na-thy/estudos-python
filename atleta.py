from datetime import date
ano = int(input("Digite o ano do seu nascimento: "))
data = date.today().year
idade = data - ano
if idade <= 9:
    print("O atleta tem {} anos.".format(idade))
    print("CLASSIFICAÇÃO: MIRIM.")
elif idade <= 14:
    print("O atleta tem {} anos.".format(idade))
    print("CLASSIFICAÇÃO: INFANTIL.")
elif idade <= 19:
    print("O atleta tem {} anos.".format(idade))
    print("CLASSIFICAÇÃO: JUNIOR.")
elif idade <= 25:
    print("O atleta tem {} anos.".format(idade))
    print("CLASSIFICAÇÃO: SÊNIOR.")
else:
    print("O atleta tem {} anos.".format(idade))
    print("CLASSIFICAÇÃO: MASTER.")