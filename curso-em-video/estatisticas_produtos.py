lista_produtos = []
lista_precos = []
total = 0
quantos_produtos_maior_valor = 0
menor = 0
cont = 0
barato = ''


while True:
    produto = str(input('Qual o nome do produto: '))
    lista_produtos.append(produto)
    preco = float(input('Qual o valor do produto: R$ '))
    lista_precos.append(preco)
    total += preco
    cont += 1
    barato = produto

    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    if preco >= 1000:
        quantos_produtos_maior_valor += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Tem mais item na sua compra [S/N]:')).upper().strip()[0]
  
    if continuar == 'N':
        break

print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {quantos_produtos_maior_valor} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')

