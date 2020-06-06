def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

pos = int(input('Informe posição do fibonacci: '))
resultado = fibonacci(pos)
print('O Fibonacci é: {}'.format(resultado))