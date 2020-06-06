salario_bruto = float(input('Informe seu salário: R$'))
tem_dependente = input('Possui dependente(s): ').upper()

if tem_dependente == 'S':
    num_dependentes = int(input('Quantos: '))
    valor_dependentes = 189.59*num_dependentes
else:
    valor_dependentes = 0

print('Valor Dependente: {:.2f}'.format(valor_dependentes))

if salario_bruto <= 1045.00:
    inss = salario_bruto*0.075   
elif salario_bruto <= 2089.60:
    inss = salario_bruto*0.090
elif salario_bruto <= 3134.40:
    inss = salario_bruto*0.12 
elif salario_bruto <= 6101.06:
    inss = salario_bruto*0.14
else:
    inss = 6101.06*0.14

print('INSS: {:.2f}'.format(inss))

bc = salario_bruto - inss - valor_dependentes
print('Base Cálculo: {:.2f}'.format(bc))

if bc < 1903.99:
    irpf = 0
elif bc <= 2826.65:
    irpf = bc*0.075-142.80
elif bc <= 3751.05:
    irpf = bc*0.15-354.80
elif bc <= 4664.68:
    irpf = bc*0.225-638.13
else:
    irpf = 4664.68*0.275-869.36

print('IRPF: {:.2f}'.format(irpf))

sl = salario_bruto - inss - irpf

print('Salário líquido: {:.2f}'.format(sl))
