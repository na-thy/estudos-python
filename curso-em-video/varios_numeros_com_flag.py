n = s = 0
cont = 0
while True:
    n = int(input('Digite um número (para parar digite 999): '))
    if n == 999:
        break
    s+=n
    cont += 1
    
print(f'A soma vale {s}\nForam digitados {cont} números.')