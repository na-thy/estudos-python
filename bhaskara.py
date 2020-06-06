import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - 4 * a * c

if delta >= 0:
    x1= -(b) + math.sqrt(delta)
    x1_final = x1/(2*a)

    x2= -(b) - math.sqrt(delta)
    x2_final = x2/(2*a)

if delta <= 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    print("a raiz desta equação é",x1_final)
elif x1_final<=x2_final:
    print("as raízes da equação são",x1_final, "e",x2_final) 
else:
    print("as raízes da equação são",x2_final, "e",x1_final)

    
