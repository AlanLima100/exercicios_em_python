#CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA: [1] SOMR [2] MULTIPLICAR [3] MAIOR [4] NOVOS NÚMEROS [5] SAIR DO PROGRAMA.
import time
num = float(input("Digite um número:").strip())
num2 = float(input("Digite outro número:").strip())
print("O que você deseja fazer com esses dois números?...")
print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
     \n""")

opção = int(input("Qual é a sua opção:"))

while opção != 5:

    if opção == 1:
        print(" \033[32mA Soma entre {} + {} = {}\033[m".format(num, num2, num + num2))
    if opção == 2:
        print("\033[33mA multiplicação entre {} X {} = {}\033[m".format(num, num2, num * num2))
    if opção == 3:
        if num > num2:
            print("\033[34mO maior número entre {} e {} é o {}\033[m".format(num, num2, num))
        else:
            print("\033[34mO maior número entre {} e {} é o > {} <\033[m".format(num, num2, num2))
    if opção == 4:
        print("\033[35mQuais número você quer novamente?..\033[m")
        num = float(input("Primeiro valor:").strip())
        num2 = float(input("Segundo valor:").strip())
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa\n""")
    if opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
        print("\033[1;31mopção invalida, tente novamente!\033[m")
        print("""
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos números
            [5] sair do programa\n""")
    opção = float(input("Nova opção?:").strip())
    if opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
        print("\033[1;31mopção invalida, tente novamente!\033[m")
        print("""
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos números
            [5] sair do programa\n""")
        opção = float(input("Nova opção?:").strip())
print("PROCESSANDO...")
time.sleep(2)
print("\033[36mChegamos ao fim, até breve!\n")

#COMO PROFESSOR FEZ DEPOIS DE EU TER FEITO:

# from time import sleep
# n1 = int(input("Primeiro valor:"))
# n2 = int(input("Segundo valor:"))
# opção = 0
# while opção != 5:
#     print("""
#                 [1] somar
#                 [2] multiplicar
#                 [3] maior
#                 [4] novos números
#                 [5] sair do programa\n""")
#     opção = int(input(">>Qual é a sua opção:?"))
#     if opção == 1:
#         soma = n1 + n2
#         print("A soma entre {} + {} é {}".format(n1, n2, soma))
#     elif opção == 2:
#         produto = n1 * n2
#         print("O resultado de {} x {} é {}".format(n1, n2, produto))
#     elif opção ==3:
#         if n1 > n2:
#             maior = n1
#         else:
#             maior = n2
#         print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))
#     elif opção == 4:
#         print("Informe os números novamente:")
#         n1 = int(input("Primeiro valor:"))
#         n2 = int(input("Segundo valor:"))
#     elif opção == 5:
#         print("finalizando...")
#     else:
#         print("Opção inválida. Tente novamente")
#     print("=-="*10)
#     sleep(2)
# print("Fim do programa! Volte sempre!")








#PRIMEIRA TENTATIVA QUE EU FIZ:
# opção = 0
# num = int(input("Digite um número:").strip())
# num2 = int(input("Digite outro número:").strip())
# print("O que você deseja fazer com esses dois números?...")
# print("""
#     [1] somar
#     [2] multiplicar
#     [3] maior
#     [4] novos números
#     [5] sair do programa\n""")
#
# while opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
#     opção = int(input("Qual é a sua opção:"))
#     if opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
#         print("\033[1;31mopção invalida, tente novamente!\033[m")
#         print("""
#             [1] somar
#             [2] multiplicar
#             [3] maior
#             [4] novos números
#             [5] sair do programa\n""")
#         opção = int(input("Nova opção?:"))
#     if opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
#         print("\033[1;31mopção invalida, tente novamente!\033[m")
#         print("""
#                     [1] somar
#                     [2] multiplicar
#                     [3] maior
#                     [4] novos números
#                     [5] sair do programa\n""")
#         opção = int(input("Nova opção?:"))
# while opção != 5:
#
#     if opção == 1:
#         print(" \033[32mA Soma entre {} + {} = {}\033[m".format(num, num2, num + num2))
#     if opção == 2:
#         print("\033[33mA multiplicação entre {} X {} = {}\033[m".format(num, num2, num * num2))
#     if opção == 3:
#         if num > num2:
#             print("\033[34mO maior número entre {} e {} é o {}\033[m".format(num, num2, num))
#         else:
#             print("\033[34mO maior número entre {} e {} é o > {} <\033[m".format(num, num2, num2))
#     if opção == 4:
#         print("\033[35mQuais número você quer novamente?..\033[m")
#         num = int(input("Primeiro valor:"))
#         num2 = int(input("Segundo valor:"))
#     print("""
#     [1] somar
#     [2] multiplicar
#     [3] maior
#     [4] novos números
#     [5] sair do programa\n""")
#     opção = int(input("Nova opção?:"))
#     if opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
#         print("\033[1;31mopção invalida, tente novamente!\033[m")
#         print("""
#             [1] somar
#             [2] multiplicar
#             [3] maior
#             [4] novos números
#             [5] sair do programa\n""")
#         opção = int(input("Nova opção?:"))
#
# print("Chegamos ao fim, até breve!\n")
