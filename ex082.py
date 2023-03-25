#CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLCOAR EM UMA LISTA. DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APEAS OS VALORES PARES E OS VALORES IMPARES DIGITAS, RESPECTIVAMENTE
# aO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS.
lista1 = []
pares = []
impares = []
while True:
    num = int(input("Digite um número:"))
    t = str(input("Quer continuar? [S/N]")).strip().upper()
    lista1.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 == 1:
        impares.append(num)
    if t == "N":
        break
    while t not in "sSnN":
        t = str(input("Valor inválido, Quer continuar? [S/N]")).strip().upper()
        if t == "N":
            break
lista1.sort()
pares.sort()
impares.sort()
print(f"Todos os números da lista são → \033[31m{lista1}\033[m")
print(f"Esses são os números pares → \033[35m{pares}\033[m")
print(f"Esses são os núemros ímpares → \033[32m{impares}")


# COMO O PROFESSOR FEZ:
# num = list()
# pares = list()
# impares = list()
#
# while True:
#     num.append(int(input("Digite uim número:")))
#     resp = str(input("Quer continuar? [S/N]:"))
#     if resp in "Nn": #Estou falando aqui → se a resposta (resp) estiver entre "nN" maiusculo ou minusculo
#         break
# for i, v in enumerate(num): #indice e valor o "i" é o contador
#     if v % 2 == 0: # o "v" aqui é o valor que foi digitado em num.append() o que o usuário digitou
#         pares.append(v)
#     elif v % 2 == 1:
#         impares.append(v)
# print("-=" * 30)
# print(f"A lista completa é {num}")
# print(f"A lista de pares é {pares}")
# print(f"A lsita de ímpares é {impares} ")


lanche = [" ","hamburguer",   "suco",   "pizza", "pudim"]
# print(lanche) #- vai mostrar  (  "hamburguer",   "suco",   "pizza", "pudim")
#
#
# lanche = ("hamburguer",   "suco",   "pizza", "pudim")
# print(lanche[1]) #- vai mostrar o "suco" na posição "1"
#
# for pos, comida in enumerate(lanche): # ele me dá tento os dados quanto a posição
#     print(f"Eu vou comer {comida} na posição  {pos}")


# for cont in range(0, len(lanche)): # "cont" na posição (zero)
for cont in range(1, 5):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")


