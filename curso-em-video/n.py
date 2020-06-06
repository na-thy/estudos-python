numero0 = int(input("Digite um número:"))
numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite um número:"))
numero3 = int(input("Digite um número:"))
numero4 = int(input("Digite um número:"))
numero5 = int(input("Digite um número:"))

par = 0
impar = 0 

resultado0 = numero0 % 2 == 0
if resultado0:
    par = par + 1 
else:
    impar = impar + 1

resultado1 = numero1 % 2 == 0
if resultado1:
    par = par + 1 
else:
    impar = impar + 1

resultado2 = numero2 % 2 == 0
if resultado2:
    par == par + 1
else:
    impar = impar + 1

resultado3 = numero3 % 2 == 0 
if resultado3:
    par = par + 1 
else:
    impar = impar + 1

resultado4 = numero4 % 2 == 0 
if resultado4:
    par = par + 1 
else:
    impar = impar + 1

resultado5 = numero5 % 2 == 0 
if resultado5:
    par = par + 1 
else:
    impar = impar + 1

print ("PAR:", par)
print ("ÍMPAR:", impar)


