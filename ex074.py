#CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA. DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.
from random import randint
num = randint(0, 10)
num1 = randint(0, 10)
num2 = randint(0, 10)
num3 = randint(0, 10)
num4 = randint(0, 10)

numeros = (num, num1, num2, num3, num4)
print(numeros)

print(f"O maior número foi {max(numeros)}")
print(f"E o menor número foi {min(numeros)}")

#PROFESSOR FEZ

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print("Os valores sorteados foram:", end="")
for n in numeros: # para cada elemento dentro de numeros me mostre: "n"
    print(f"{n} ", end="")
print(f"\nO maior número foi {max(numeros)}")
print(f"E o menor número foi {min(numeros)}")



