"""def fibo(n):
    if n < 2:
        return n

    else:
        res = fibo(n-1) + fibo(n-2)
        return res"""

def fibo_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
    return res

n = eval(input('Valor de Fibonacci: '))

resultado = fibo_it(n)
print(resultado)
