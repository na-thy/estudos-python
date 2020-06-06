import math
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))

x1 = a
y1 = b
x2 = c
y2 = d

dxy = ((x1 + x2)**2) + ((y1 + y2)**2)
dxy_final = math.sqrt (dxy)

if (dxy_final) >= 10:
    print ("Longe")

else: 
    print ("Perto")

