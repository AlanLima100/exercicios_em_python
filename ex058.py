# Melhore o jogo do DESAGIO 028 onde o computador vai "pensar" em um número de 0 e 10. Só que agora adivinhar até acetar, mostrando no final quantos palpites foram necessários para
#vencer.
t = 0
r = 0
tentativas = 0
tentativas1 = 0
tentativas2 = 0
from random import randint
from time import sleep # faz o computador esperar, dormir por alguns segundos
computador = randint(0, 10)
print("Olá eu sou o seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue advinhar qual foi?")
jogador = int(input("Qual é o seu palpite?:"))
print("PROCESSANDO...")
sleep(3)
while jogador != computador:
    if jogador > computador:
        print("Menos...")
        jogador = int(input("Tente outra vez!:"))
        tentativas = tentativas + 1
    else:
        print("Mais...")
        jogador = int(input("Tente outra vez!:"))
        tentativas1 = tentativas1 + 1
tentativas2 = tentativas + tentativas1
print("VOCÊ ACERTOU!! COM {} TENTATIVA(as). PARABÉNS!!".format(tentativas2 + 1))

#COMO O PROFESSOR FEZ:

from random import randint
computador = randint(0, 10)
print("Sou seu computaor... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpites = 0
while not acertou: # enquanto não acertou
    jogador = int(input("Qual é seu palpite?"))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente mais uma vez.")
        elif jogador > computador:
            print("Mais...Tente mais uma vez")
print("Acertou com {} tentativas. PARABÉNS!".format(palpites))



