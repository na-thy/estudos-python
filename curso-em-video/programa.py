import math
n = int(input("Digite um número: "))

n1 = n+1
n2 = n-1
ndobro = n*2
ntriplo = n*3
nraiz = math.sqrt(n)
# a raiz também pode ser calculada nraiz = n**(1/2)

print("O sucessor de {} é {} e o antecessor é {}.".format(n,n1,n2))
print("O dobro de {} é {}".format(n,ndobro))
print("O triplo de {} é {}".format(n,ntriplo))
print("A raiz quadrada de {} é {:.2f}".format(n,nraiz))
