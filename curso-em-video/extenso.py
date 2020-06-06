numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    digitar = int(input("Digite um número entre 0 e 20: " ))
    if digitar >= 0 and digitar <= 20:
        break
print(f'Você digitou o número: {numeros[digitar]}')

#for c, numero in enumerate(numeros):
#   if digitar == c:
#       print(numero)