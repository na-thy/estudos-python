salario = float(input("Digite o valor do salário: "))

salario_final = salario + (salario * 15//100)

print("O salário final é R$ {:.2f}".format(salario_final))
