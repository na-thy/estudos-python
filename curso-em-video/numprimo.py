n = int(input("Digite um número para saber se ele é número primo: "))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        tot += 1
        print("\033[33m{}\033[m".format(c),end=" ")
    else:
        print("\033[31m{}\033[m".format(c),end=" ")
print("\n""O número {} foi divisível {} vezes.".format(n, tot))
if tot == 2:
    print("É número primo.")
else:
    print("Não é número primo.")
