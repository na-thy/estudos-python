mulheres_menos_20 = 0
homens = 0
pessoas_com_mais_18 = 0

while True:
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo [F/M]: ')).upper().strip()[0]
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if idade >= 18:
        pessoas_com_mais_18 += 1
    if sexo == 'F': 
        if idade <= 20:
            mulheres_menos_20 += 1
    elif sexo == 'M':
        homens += 1

    if continuar == 'N':
        break

print(f'No cadastro tivemos {pessoas_com_mais_18} pessoa(s) cadastrada(s) com mais de 18 anos.')
print(f'No cadastro tivemos {mulheres_menos_20} mulher(es) menor(es) de 20 anos.')
print(f'No cadastro tivemos {homens} homem(ns) cadastrado(s).')