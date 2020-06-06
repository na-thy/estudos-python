from math import hypot 

coposto = float(input("Digite o valor do cateto oposto: "))
cadjacente = float(input("Digite o valor do cateto adjacente: "))

hi = hypot(coposto, cadjacente)

print("A hipotenusa vai medir {:.2f}".format(hi))