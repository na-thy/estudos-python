def calcula_media(n1,n2,n3):
    soma = 1/(n1+4)+1/(n2+4)+1/(n3+4)
    return 3/soma - 4

nota1 = eval(input('Digite o valor da nota 1: '))
nota2 = eval(input('Digite o valor da nota 2: '))
nota3 = eval(input('Digite o valor da nota 3: '))

media = calcula_media(nota1,nota2,nota3)

if media >= 5:
    print('Aprovado com média ', media)

else:
    print('Reprovado com média ', media)
