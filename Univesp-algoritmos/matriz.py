matrizA = [[0,0,0], [0,0,0], [0,0,0]]
matrizB = [[0,0,0], [0,0,0], [0,0,0]]
soma =    [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(0, 3):
    for colunas in range(0, 3):
        matrizA[linha][colunas] = int(input(f'Digite um valor para a Matriz A: '))
print('**' * 30)

for linha in range(0, 3):
    for colunas in range(0, 3):
        matrizB[linha][colunas] = int(input(f'Digite um valor para a Matriz B: '))
print('**' * 30)

for linha in range(0, 3):
    for colunas in range(0,3):
        soma[linha][colunas] = matrizA[linha][colunas] + matrizB[linha][colunas]

print(soma)


