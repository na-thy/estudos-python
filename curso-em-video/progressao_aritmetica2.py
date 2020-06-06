print('Gerador de Progressão Aritmética')
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = t 
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end=' ')
        termo += r
        cont += 1
    print('Pausa')  
    mais = int(input('Quantos termos você quer mostrar a mais: '))
    
print(f'Sua progressão aritmética foi finalizada com {total} termos mostrados.')
'\n'