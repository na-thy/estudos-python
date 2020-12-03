# () são tuplas
# tuplas são imutáveis(não posso alterar o valor no programa rodando, só nele parado)
lanche = ('Hambúrguer','Suco', 'Pizza', 'Pudim', 'Batata Frita')

#for comida in lanche:
#    print(f'Eu vou comer {comida}')

for comida in range(0, len(lanche)):
    print(f' Eu vou comer pra carambra {lanche[comida]} na posição {comida}')

#for pos,comida in enumerate(lanche):
#    print(f'Comi pra caramba {comida} na posição {pos}')

print(sorted(lanche))


a = (2,5,4)

b = (5,8,1,2)
c = b + a
print(c)
print(f'Quantas vezes o número 5 aparece na lista {c.count(5)}')
print(f'O número 8 está na posição {c.index(8)}')

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)