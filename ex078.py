# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIFITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.

lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {cont}°:')))
print(f'Você digitou os valores {lista}')
print(f'O maior número digitado foi {max(lista)} que está nas posições {lista.index(max(lista))}°', end="")
for c, v in enumerate(lista):
    if v == max(lista):
        print(f"{c}...")
print(f"O menor número digitado foi {min(lista)} que está nas posições {lista.index(min(lista))}°", end="")
for c, v in enumerate(lista):
    if v == min(lista):
        print(f"{c}...")


#COMO O PROFESSOR FEZ:

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f"Digite um valor para a posição {c}")))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print("=-" * 30)
print(f"Você digitou os valores {listanum}")
print(f"O maior valor digitado foi {mai} nas posições", end="")
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {men} nas posições", end="")
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}...", end="")
print()
