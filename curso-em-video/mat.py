import math
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b**2 - 4 * a * c

if delta == 0:
    x1= (-(b) + math.sqrt(delta)) / (2*a)
    print ("A raiz de desta equação é", x1)
else:
    if delta < 0:
        print ("Está equação não possui raiz")
    else:
        x1= (-(b) + math.sqrt(delta)) / (2*a)
        x2= (-(b) - math.sqrt(delta)) / (2*a)
        print ("As raízes desta equação são", x1, "e", x2)






