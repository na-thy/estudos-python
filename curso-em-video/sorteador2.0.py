from random import randint
computador = 1
jogador = 0
tentativa = 0
print("             \033[0;33mVamos jogar novamente!\033[m")
print("Mas dessa vez eu só vou parar quando você acertar o número que eu pensei...")
print("Vou pensar em um número de 0 a 10.")

while computador != jogador:
    computador = randint(0,10)
    jogador = int(input("Digite o número que você acha que eu pensei...: "))
    if computador != jogador:
        tentativa += 1
        print("\033[0;31m       Tente novamente\033[m")
        print("Eu pensei \033[0;31m{}\033[m e você pensou \033[0;31m{}\033[m.".format(computador,jogador))

print("Você precisou de \033[0;32m{}\033[m chances para acertar.".format(tentativa))
print("\033[0;32m       Uau.... Você acertou!\033[m")
print("Eu pensei \033[0;32m{}\033[m e você também pensou \033[0;32m{}\033[m.".format(computador,jogador))

