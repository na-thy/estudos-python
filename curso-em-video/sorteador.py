from random import randint
from time import sleep
print("-=-"*30)
a = ("""-- Quero ver se você é mais esperto que eu! \nVou pensar em um número de 0 a 5! tente descobrir que número eu pensei... --""").upper()
print(a)
print("-=-"*30)
jogador= int(input("Digite um número de 0 a 5: "))
print("-=-"*30)
computador = randint(0,5)
print("PROCESSANDO...")
sleep(2)
print("EU PENSEI NO NÚMERO {}".format(computador))

if jogador == computador:
    print("POXA VIDA!!! VOCÊ ACERTOU!!!")
else:
    print("EU VENCI.")
print("--FIM--")
