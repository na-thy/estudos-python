quantidade = int(input('Quantos produtos deseja cadastrar: '))
i = 0 

produto = [0] * quantidade
quantidade_vendida = [0] * quantidade
valor = [0] * quantidade
valor_total_produtos = [0] * quantidade

while (i < quantidade):
    print(' ')
    produto[i] = str(input('Digite o nome do produto: '))
    quantidade_vendida[i] = int(input('Quantidade vendida: '))
    valor[i] = float(input('Valor unitário: '))
    valor_total_produtos[i] = quantidade_vendida[i] * valor[i]
    print(' ')
    print(f'Lucro deste produto: R${valor_total_produtos[i]:.2f}')
    i +=1

valor_final = sum(valor_total_produtos)

print(' ')
print(f'Lucro total: R${valor_final:.2f}')

print('Fim')
