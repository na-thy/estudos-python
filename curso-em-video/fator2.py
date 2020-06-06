fatorial = int(input('Digite o fatorial de n: '))

resultado = 1
conta = 1

while conta <= fatorial:
    resultado *= conta
    conta += 1
print(resultado)
