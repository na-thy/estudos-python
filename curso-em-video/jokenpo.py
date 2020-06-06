import emoji
from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print("*."*20)
print("VAMOS JOGAR JOKENPÔ?")
print("[0] PEDRA\n[1] PAPEL\n[2] TESOURA")
print("*."*20)
jogador = int(input("Digite o número que deseja jogar correspondente a lista acima: "))
print("PROCESSANDO...")
sleep(2)

if jogador == 0 and computador == 0:
    print(emoji.emojize(':fist:', use_aliases=True))
    print("\033[0;33mEmpatou.\033[m")
elif jogador == 0 and computador == 1:
    print(emoji.emojize(':fist: X :raised_hand:', use_aliases=True))
    print("\033[0;31mEu Ganhei!\033[m")
elif jogador == 0 and computador == 2:
    print(emoji.emojize(':fist: X :v:', use_aliases=True))
    print("\033[0;36mVocê Ganhou!\033[m")
elif jogador == 1 and computador == 0:
    print(emoji.emojize(':raised_hand: X :fist:', use_aliases=True))
    print("\033[0;36mVocê Ganhou!\033[m")
elif jogador == 1 and computador == 1:
    print(emoji.emojize(':raised_hand:', use_aliases=True))
    print("\033[0;33mEmpatou.\033[m")
elif jogador == 1 and computador == 2:
    print(emoji.emojize(':raised_hand: X :v:', use_aliases=True))
    print("\033[0;31mEu Ganhei!\033[m")
elif jogador == 2 and computador == 0:
    print(emoji.emojize(':v: X :fist:', use_aliases=True))
    print("\033[0;31mEu Ganhei!\033[m")
elif jogador == 2 and computador == 1:
    print(emoji.emojize(':v: X :raised_hand:', use_aliases=True))
    print("\033[0;36mVocê Ganhou!\033[m")
elif jogador == 2 and computador == 2:
    print(emoji.emojize(':v:', use_aliases=True))
    print("\033[0;33mEmpatou.\033[m")