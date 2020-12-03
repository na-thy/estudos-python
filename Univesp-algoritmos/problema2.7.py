'''Problema Prático 2.7
Dada a lista de notas de trabalho de casa dos alunos
>>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2] escreva:
(a)Uma expressão que mostre quantas vezes 7 aparece.
(b)Uma instrução que muda a última nota para 4.
(c)Uma expressão que avalia para a nota mais alta.
(d)Uma instrução que classifica as notas da lista.
(e)Uma expressão que avalia para a média das notas.'''

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas)

'''(a)Uma expressão que mostre quantas vezes '7' aparece.'''
a = notas.count(7)
'''(b)Uma instrução que muda a última nota para 4.'''
b = notas[-1] = 4
'''(c)Uma expressão que avalia para a nota mais alta.'''
c = max(notas)
'''(d)Uma instrução que classifica as notas da lista.'''
d = notas.sort()
'''(e)Uma expressão que avalia para a média das notas.'''
e = sum(notas)/len(notas)

print(a,b,c,notas,e)