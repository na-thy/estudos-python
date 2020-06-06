from random import randint
from operator import itemgetter

jogo = {"jodador1": randint(1,6),
        "jogador2": randint(1,6),
        "jogador3": randint(1,6),
        "jogador4": randint(1,6)
        }


ranking = {}
print("Valores sorteados: ")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)