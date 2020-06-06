valor = int(input('Que valor você quer sacar: R$: '))

cinquenta = valor // 50 
resto =  valor % 50
valor_ajustado = valor - 50*cinquenta

vinte = valor_ajustado // 20
resto_vinte = valor_ajustado % 20

dez = resto_vinte // 10
resto_dez = resto_vinte % 10

um = resto_dez // 1

print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')

