'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor = eval(input('Quanto vale a sua hora: '))
horas = eval(input('Quantas horas você trabalhou esse mês: '))

resultado = valor * horas

print('Você trabalhou ', horas, 'horas e recebeu ', resultado)