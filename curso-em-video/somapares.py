soma = 0
conta = 0
for n in range(0,6):
    n = int(input("Digite números a serem somados: "))
    if n % 2 == 0:
        soma += n
        conta += 1
print("A sequência dos seus números, tiveram {} números pares.".format(conta))
print("A soma dos números pares foi {}.".format(soma))
