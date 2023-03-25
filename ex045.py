#CRIE UM PROGMRA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ:

import random
from time import sleep
computador = random.randint(0, 2)
print("-=-" * 30)
print("Escolha sua opção no Jokenpô...")
print(""" 
[0] pedra
[1] papel
[2] tesoura""")
print("-=-" * 30)
jogador = int(input("Qual é sua JOGADA?:"))
itens = ("Pedra", "Papel", "Tesoura")

sleep(0)
print("JO")
sleep(0.5)
print('KEN')
sleep(1)
print("POO !!!""")
print("-=-" * 30)
print('Computador escolheu {}'.format(itens[computador]))
print("Jogador escolheu {}".format(itens[jogador]))
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print("EMPATE JOGUEM DE NOVO!!!!")
        print("-=-" * 30)
    elif jogador == 1:
        print("JOGADOR VENCEU")
        print("-=-" * 30)
    elif jogador == 2:
        print("COMPUTADOR VENCEU!!")
        print("-=-" * 30)
    else:
        print("JOGADA INVÁLIDA")
        print("-=-" * 30)
elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 1:
        print("EMPATE JOGUEM DE NOVO!!")
        print("-=-" * 30)
    elif jogador == 2:
        print("JOGADOR VENCEDOR!!")
        print("-=-" * 30)
    elif jogador == 0:
        print(" COMPUTADOR VENCEU!!")
        print("-=-" * 30)
    else:
        print("JOGADA INVÁLIDA")
        print("-=-" * 30)
elif computador == 2:
    if jogador == 2:
        print("EMPATE JOGUEM DE NOVO!!")
        print("-=-" * 30)
    elif jogador == 1:
        print("COMPUTADOR VENCEU")
        print("-=-" * 30)
    elif jogador == 0:
        print("JOGADOR VENCEU!!")
        print("-=-" * 30)
    else:
        print("JOGADA INVÁLIDA!")
        print("-=-" * 30)


# elif random.choice(lista) == 2 and opcao == 2:
#     print("EMPATE JOGUEM DE NOVO!!!!")
#
# elif random.choice(lista) == 3 and opcao == 1:
#     print("-=-" * 30)
#     print("JOGADOR VENCEU!!")
# elif random.choice(lista) == 1 and opcao == 2:
#     print("-=-" * 30)
#     print("JOGADOR VENDEU!!")
# elif random.choice(lista) == 1 and opcao == 1:
#     print("-=-" * 30)
#     print("EMPATE JOGUEM DE NOVO!!")
# elif random.choice(lista) == 2 and opcao == 3:
#     print("-=-" * 30)
#     print("JOGADOR VENCEU!!")
# elif random.choice(lista) == 2 and opcao == 1:
#     print("-=-" * 30)
#     print("COMPUTADOR VENCEU!!")
# elif random.choice(lista) == 3 and opcao == 1:
#     print("-=-" * 30)
#     print("JOGADOR VENCEU!!")
# elif random.choice(lista) == 3 and opcao == 2:
#     print("-=-" * 30)
#     print("COMPUTADOR VENCEU!!")
# elif random.choice(lista) == 3 and opcao == 3:
#     print("-=-" * 30)
#     print("EMPRATE JOGUEM DE NOVO!!")



