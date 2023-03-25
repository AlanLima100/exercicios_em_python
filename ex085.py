#Crie um programa onde o usuário poss digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. no final, moster os valores
# pares e ímpares em  ordem crescente.
lista = []
pares = []
impares = []
for p in range(0, 7):
    lista.append(int(input("Digite um valor:")))
for g in lista:
    if g % 2 == 0:
        pares.append(g)
    else:
        impares.append(g)
pares.sort()
impares.sort()
print(f"Os valores pares digitados foram: {pares}")
print(f"os valores ímpares digitados foram {impares}")


#Como o professor:

num = [[], []] #ele colocou lista dentro da lista com essa técnica
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}° valor~:"))
    if valor % 2 == 0: # Se o valor dividido por 2 e o resto da dividão for igual a zero...
        num[0].append(valor)# adicione o resultado que será um número par dentro de num na lista 0 (zero) a primeira da esquerda para direita.
    else:
        num[1].append(valor) # se não adicione em na segunda lista dentro de num da direita para esquerda, que será um valor impar
print("-=" * 30)
num[0].sort() # tudo que estiver dentro de num na primeira lista, vai ser colocado em ordem
num[1].sort() # Tudo que estiver dentro de num na segunda lista, vai ser colocado em ordem
print(f"Os valores pares digitados foram: {num[0]}")
print(f"os valores ímpares digitados foram {num[1]}")
