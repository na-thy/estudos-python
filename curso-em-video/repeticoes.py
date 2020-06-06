n = int(input("Digite o valor de n (n > 0): "))
d = int(input("Digite o valor de d (0<=d<=9): "))

conta_digito = 0
n_salvo = n
while n > 0:
    dig = n % 10
    n = n // 10
    if dig == d:
        conta_digito = conta_digito + 1

print("O digito", d, "ocorre", conta_digito, "vezes em ", n_salvo)






