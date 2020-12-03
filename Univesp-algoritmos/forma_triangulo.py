a = eval(input('Informe o valor do lado 1: '))
b = eval(input('Informe o valor do lado 2: '))
c = eval(input('Informe o valor do lado 3: '))

maior_lado = max(a,b,c)

if maior_lado < a + b + c - maior_lado:
    print('Os lados formam um triângulo.')
    if a == b and b == c and c == a:
        print('Triângulo Equilátero.')
    elif a != b and b != c and c!= a:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles.')
else:
    print('Os lados não formam um triângulo.')
