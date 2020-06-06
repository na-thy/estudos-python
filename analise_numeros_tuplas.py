
n = (int(input('Digite um número: ')), 
int(input('Digite o segundo número: ')),
int(input('Digite o terceiro número: ')), 
int(input('Digite o último número: ')))

print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vez(es).')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1} posição.')
else:
    print(f'O valor 3 não foi digitado.')
print(f'Os valores pares foram', end=' ')

for c in n:
    if c % 2 == 0:
        print(c, end=' ')

