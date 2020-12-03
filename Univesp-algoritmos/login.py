lista = ['Joe', 'Sue', 'Hani', 'Sofia']

nome = input('Digite seu nome: ')

if nome in lista:
    print('Login:', nome)
    print('Você está logado!')
else:
    print('Login:', nome)
    print('Acesso negado! ')