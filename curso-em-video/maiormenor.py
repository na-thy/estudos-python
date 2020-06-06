a = int(input("Digite um número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a < b and a < c and b < c:
    print("O valor {} é menor e o valor {} é maior.".format(a,c))

if a > b and a > c and b < c:
    print("O valor {} é menor e o valor {} é maior.".format(b,a))

if a < b and a < c and b > c:
    print("O valor {} é menor e o valor {} é maior.".format(a,b))

if a < b and a > c and b > c:
    print("O valor {} é menor e o valor {} é maior.".format(a,b))

if b < a and b > c and c < a:
    print("O valor {} é menor e o valor {} é maior.".format(c,a))

if a < c and b < a and c > b:
    print("O valor {} é menor e o valor {} é maior.".format(b,c))

if a == b and a < c:
    print("O valor {} é menor e o valor {} é maior.".format(a,c))

if a == c and a < b:
    print("O valor {} é menor e o valor {} é maior.".format(a,b))

if a == c and a > b:
    print("O valor {} é menor e o valor {} é maior.".format(b,a))

if a == b and a > c:
    print("O valor {} é menor e o valor {} é maior.".format(c,a))

if b == c and a < b:
    print("O valor {} é menor e o valor {} é maior.".format(a,b))

if b == c and a > b:
    print("O valor {} é menor e o valor {} é maior.".format(b,a))