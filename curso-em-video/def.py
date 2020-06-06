def troca(vet):
    for i in range(10):
        if vet[i] >=0:
            vet[i] = 1
        else:
            vet[i] = 0 
    return vet

vet = [0]*10
for i in range(10):
    vet[i] = int(input('Digite um valor: '))
print(vet)    

troca(vet)
print(vet)


