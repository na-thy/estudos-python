print("="*40)
print(" 10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA")
print("="*40)
t = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
for c in range(0,10):
    print(t,end=" ")
    t = t + r
print("ACABOU")