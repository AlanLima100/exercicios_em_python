#FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL
# DO JOGO.
from random import randint
print("=-"*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*20)
cont = 0
vitoria = 0
while True:
    jogador = int(input("Escolha um valor:"))
    num = str(input("Par ou Ímpar [P/I]?:").upper().strip())
    while num not in "Pp" and num not in "Ii":
        num = str(input("\033[31mVALOR INVALIDO!!\033[m \033[32mPar\033[m ou \033[32mÍmpar\033[m [P/I]?:").upper().strip())
    cont = cont + 1
    computador = randint(0, 10)
    c = computador % 2
    total = jogador + computador
    n = total % 2
    par = "PAR"
    impar = "Ímpar"
    print("=-"*20)
    print(f"Você jogou {jogador} e o computador jogou {computador}")
    if n == 0:
        print(f"A Soma dos valores deu {total} {par}")
    else:
        print(f"A Soma dos valores deu {total} {impar}")
    if n == 0 and num == "P":
        print("\033[32mPARABÉNS VC GANHOU!\033[m")
        vitoria = vitoria + 1
    elif num == "I" and n == 1:
        print("\033[32mPARABÉNS VC GANHOU!\033[m")
        vitoria = vitoria + 1
    else:
        print("\033[31mVOCÊ PERDEU!! VITÓRIA DO COMPUTADOR!!\033[m")
        print("\033[31mGAMER OVER!!\033[m")
        break
    print("=-"*20)
    print("vamos jogar novamente...")
print("=-"*20)
print("\033[33mFIM DO GAME! ATÉ A PROXIMA\033[m")
print(f"\033[32mVOCÊ GANHOU {vitoria} vez(es) SEGUIDA(AS)!!")


#COMO O PROFESSOR FEZ!

# from random import randint
# v = 0
# while True:
#     jogador = int(input("Diga um valor:"))
#     computador = randint(0, 10)
#     total = jogador + computador
#     tipo = " "
#     while tipo not in "PI":
#         tipo = str(input("Par ou Ímpar? [P/I]")).strip().upper()[0]
#     print(f"Você jogou {jogador} e o computador {computador}. Total de {total}", end="")
#     print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
#     if tipo == "P":
#         if total % 2 == 0:
#             print("Você VENCEU!")
#             v += 1
#         else:
#             print("Você PERDEU!!")
#             break
#     elif tipo == "I":
#         if total % 2 == 1:
#             print("VOCÊ VENCEU!!")
#             v += 1
#         else:
#             print("VOCE PERDEU!")
#             break
#     print("Vamos jogar novamente...")
# print(f"GAMER OVER! Você venceu {v} vezes")