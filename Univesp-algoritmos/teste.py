nota_1 = eval(input('Digite a nota da prova 1: '))
nota_2 = eval(input('Digite a nota da prova 2: '))
 
media = (nota_1 * 0.4) + (nota_2 * 0.6)

if media >= 5:
    print(media)
    print('Aluno aprovado.')
else:
    print(media)
    print('Aluno reprovado.')