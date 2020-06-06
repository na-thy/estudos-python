a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    if a == b and a == c and b == c:
        print("Triângulo Equilátero.")
    elif a != b != c != a:
        print("Triângulo Escaleno.")
    elif a == b != c or b == c != a or a == c != b:
        print("Triângulo Isósceles.")
else:
    print("Não formam um triângulo.")
