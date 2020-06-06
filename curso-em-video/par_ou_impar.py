from random import randint

vitoria = 0
while True:
    jogador = int(input('Escolha um número (de 0 até 10): '))
    computador = randint(0,10)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'pi':
        escolha = str(input('Você quer par ou ímpar [P/I]: ')).lower() 
    print(f'Você jogou: {jogador}')
    print(f'O computador jogou: {computador}')
    print(f'A soma dos dois valores: {soma}')
    
    if escolha == 'p':
        if soma % 2 == 0:
            print('Você ganhou!')
            vitoria +=1
        else:
            print(f'Você perdeu.')
            break       
    elif escolha == 'i':
        if soma % 2 != 0:
            print(f'Você ganhou!')
            vitoria +=1
        else:
            print(f'Você perdeu.')
            break     
print(f'Você venceu {vitoria} vez(es)')