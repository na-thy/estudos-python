# verificar se há adjacentes iguais

n = int(input("Digite uma sequência de números: "))

adjacentes = False
anterior = n % 10
n = n // 10

while n > 0:
    r = n % 10
    if anterior == r:
        adjacentes = True
    anterior = r
    n = n // 10

if adjacentes:
    print ("Contém adjacentes iguais.")

else:
    print("Não contém adjacentes iguais.")