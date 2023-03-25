#CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEÁTÓRIOS. GUARDE ESSSES RESULTADOS EM UM DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O
#VENCEDOR TIROU O MAIOR NÚMERO NO DADO.

import random
from operator import itemgetter
from time import sleep
cont = 0
he = {}
ale = []
ali = []
ru = []
ranking = dict()
for r in range(0, 4):
    cont = cont + 1
    t = random.randint(1, 6)
    ru.append(print(f"O jogador {r + 1}° tirou {t}"))
    sleep(1)
    ali.append(cont)
    ale.append(t)
    mai = men = t
    z = list(zip(ali, ale))


he = sorted(list(zip(ali, ale)), key=itemgetter(1), reverse=True)
print("==============RANKING DOS JOGADORES===============")
for k, v in enumerate(he):
    print(f"        O {k + 1}° lugar: jogador{v[0]}, tirou {v[1]}")
    sleep(1)


# PROFESSOR FEZ:
# from random import randint
# from time import sleep
# from operator import itemgetter
# jogo = {"Jogador1": randint(1, 6),
#         "Jogador2": randint(1, 6),
#         "Jogador3": randint(1, 6),
#         "Jogador4": randint(1, 6)}
# ranking = list()
# print("Valores sorteados: ")
# for k, v in jogo.items():
#     print(f"{k} tirou {v} no dado")
#     sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print("==============RANKING DOS JOGADORES===============")
# for i, v in enumerate(ranking):
#     print(f"{i + 1}° lugar: {v[0]} com {v[1]}")
#     sleep(1)