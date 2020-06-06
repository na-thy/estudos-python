print("=-"*12)
print("MEU PYTHON, MINHA VIDA!")
print("=-"*12)
casa = int(input("Digite o valor da casa que pretende financiar: R$ "))
salario = int(input("Digite o valor do seu salário: R$ "))
anos = int(input("Em quantos anos pretende financiar? "))

anos_prestacao = anos * 12
prestacao = casa / anos_prestacao

if prestacao <= salario * 0.3:
    print("CONCEDIDO!\nO valor da prestação anual será de R${:.2f}.".format(prestacao))

else:
    print("NEGADO!\nO valor da prestaçaõ excede o limite permitido.")