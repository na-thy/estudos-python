x = int(input("Digite a distância da viagem: "))

if x <= 200:
    preco = x * 0.50
    
else:
    preco = x * 0.45

print("O valor da passagem é R$ {:.2f}".format(preco))