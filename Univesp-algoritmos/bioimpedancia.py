altura = input('Digite a sua altura: ')
sexo = input('Digite H para Homens e M para Mulheres: ').upper()

alt = eval(altura)

if sexo == 'H': 
    peso = (72.7 * alt) - 58
else:
    peso = (62.1 * alt) - 44.7

print('O peso ideal é: ', peso)