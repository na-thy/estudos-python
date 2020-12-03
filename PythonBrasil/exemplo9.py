def celsius(f):
    c = 5 * ((f-32)/9)
    return c

f = eval(input('Digite a temperatura em Fahrenheit para ser transformada em Celsius: '))

print(celsius(f))
