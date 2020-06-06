import math

def calculo(r):
    area = math.pi * r**2
    return area

raio = int(input('Informe raio do círculo em metros: '))

print(calculo(raio))