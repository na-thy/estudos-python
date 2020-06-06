n = int(input("Digite um número: "))
contador = 0
for c in range(1,n+1):
    if n == 2 or n == 5 or n == 9 or n % 2 != 0:
        print("{} é primo.".format(c))
    else:
        print("{} não é primo.".format(c))
        