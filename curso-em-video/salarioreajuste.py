salario = int(input("Informe o valor do seu salário: R$ "))

salario10 = salario + (salario * 0.10)
salario15 = salario + (salario * 0.15)

if salario >= 1250:
    print("O seu salário reajustado será R${:.2f}\n".format(salario10))

else:
    print("O seu salário reajustado será R${:.2f}\n".format(salario15))