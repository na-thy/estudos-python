dias = int(input("Qual a quantidade de dias o carro foi alugado: "))
km = float(input("Quantos kilometros foram rodados: "))

dias_alugados = dias * 60.00
km_rodados = km * 0.15
preco = dias_alugados + km_rodados

print("O valor do aluguel foi de R${:.2f}".format(preco))