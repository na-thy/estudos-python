from time import sleep
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
escolha = ' '

while escolha != 5:
    print("     \033[1;36mMENU\033[m")
    print("""[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa""")
    escolha = int(input("Com base nos números digitados, escolha uma opção acima: "))    
    if escolha == 1:
        soma = n1+n2
        print(f'A soma de {n1} + {n2} = {soma}.')
    elif escolha == 2:
        multiplicacao = n1*n2
        print(f'A multiplicação de {n1} * {n2} = {multiplicacao}.')
    elif escolha == 3:
        lista = [n1,n2]
        maior = max(lista)
        print(f'O maior valor entre {n1} e {n2} é {maior}.')
    elif escolha == 4:
        print('Informe novamente')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Você saiu do programa.')
        break
    else:
        print('Inválido')
    print('*-'*20)
    sleep(2)    
