# FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E VAI SORTEAR 6 NÚMEROS ENTRE 1 A 60 PARA CADA JOGO
# CADASTRANDO TUDO EM UMA LISTA COMPOSTA.
import random
import time
cont = 0
print("-=" * 30)
print("JOGA NA MEGA-SENA".center(55))
print("-=" * 30)
jogos = int(input("Quantos jogos você quer que eu sorteie?: "))
for z in range(0, jogos):
    cont = cont + 1
    print(f"JOGO {cont}: {random.sample(range(61), 6)}")
    time.sleep(1)
print("-=" * 20)
print("< BOA SORTE >".center(40))
print("-=" * 20)

# OUTRA MANEIRA EU QUE FIZ:

import random
import time
cont = 0
jogo = []
jogos = list()
f = 1
print("-=" * 30)
print("JOGA NA MEGA-SENA".center(55))
print("-=" * 30)

quant = int(input("Quantos jogos você quer que eu sorteie?: "))
print("-=" * 3, f"  SORTEANDO {quant}  JOGOS", "-=" * 3)
while f <= quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont = cont + 1
        if cont == 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    f = f + 1
cont = 0
for c in jogos:
    cont = cont + 1
    print(f"O JOGO {cont}°: {c}")
    time.sleep(1)

# OUTRA FORMA BEM SEMELHANTE A MIHA SEGUNDA OPÇÃO FEITA PELO PROFESSOR:

# from random import randint
# from time import sleep
# lista = list()
# jogos = list()
# print("-=" * 30)
# print("JOGA NA MEGA-SENA".center(55))
# print("-=" * 30)
# quant = int(input("Quantos jogos vocÇe quer que eu sorteie? "))
# print("-=" * 3, f"  SORTEANDO {quant}  JOGOS", "-=" * 3)
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont = cont + 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot = tot + 1
# for i, l in enumerate(jogos):
#     print(f"Jogo {i+1}: {l}")
#     sleep(1)

