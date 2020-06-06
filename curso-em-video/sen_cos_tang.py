import math
angulo = int(input("Digite um ângulo: "))
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
seno = math.sin(angulo)

print("O seno {:.3f}, cosseno {:.3f} e tangente {:.3f} de {}".format(seno,cosseno,tangente,angulo))