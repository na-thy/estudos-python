print("PA")
t = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
cont = 1
termo = t
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print("{} -> ".format(termo),end=" ")
        termo += r
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais: "))

print("progressão finalizada com {} termos mostrados.".format(total))