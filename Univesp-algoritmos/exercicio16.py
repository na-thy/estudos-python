# () são tuplas
# tuplas são imutáveis(não posso alterar o valor no programa rodando, só nele parado)
lanche = ('Hambúrguer','Suco', 'Pizza', 'Pudim', 'Batata Frita')

#for comida in lanche:
#    print(f'Eu vou comer {comida}')

for comida in range(0, len(lanche)):
    print(f' Eu vou comer pra carambra {lanche[comida]} na posição {comida}')

#for pos,comida in enumerate(lanche):
#    print(f'Comi pra caramba {comida} na posição {pos}')