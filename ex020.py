#SORTEANDO UMA ORDEM ALEATÓRIA NA LISTA

# import random
# n1 = str(input("Primeiro aluno:"))
# n2 = str(input("Segundo aluno:"))
# n3 = str(input("Terceiro aluno:"))
# n4 = str(input("quarto aluno:"))
#
# lista = [n1, n2, n3, n4]
# random.shuffle(lista)
# print("A ordem de apresentação será:")
# print(lista)

# PARA IMPORTAR APENAS DA BIBLIOTECA "FROM MATH IMPORT SHUFFLE

from random import shuffle
n1 = str(input("Primeiro nome:"))
n2 = str(input("Segundo nome"))
n3 = str(input("terceiro nome:"))
n4 = str(input("quarto nome:"))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(" A ordem de apresentação será:")
print(lista)
