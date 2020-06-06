x = int(input("Digite um número: "))

par = x % 2

if par == 0:
    print("O número {} é par.".format(x))

else:
    print("O número {} é ímpar.".format(x))
