# FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
# A) QUANTAS PESSOAS FORAM CADASTRADAS.
# B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
# C) UMA LISTAGEM COM AS PESSOAS MAIS LEVEZ.
#
nome = []
maior = []
menor = []
cont = 0
while True:
    nome.append([input('\nNome: '), float(input('Peso em KG: '))][::-1])

    c = str(input("Quer continuar? [S/N]")).strip().upper()
    cont = cont + 1
    while c not in "sSNn":
        c = str(input(" Valor inválido!! Quer continuar? [S/N]")).strip().upper()
    if c == "N":
        break
for p in nome:
    if p[0] == max(nome)[0]:
        maior.append(p[1])
    if p[0] == min(nome)[0]:
        menor.append(p[1])

print('=-' * 16, f"Quantidade de pessoas cadastradas: {cont}")
print(f"O maior peso foi  {max(nome)[0]}kg. peso de [{maior}]")
print(f"O menor peso foi {min(nome)[0]}kg.peso de[{menor}]")



# COMO O PROFESSOR FEZ:

# temp = []
# princ = []
# mai = men = 0
# while True:
#     temp.append(str(input("Nome:")))
#     temp.append(float(input("Peso")))
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp[1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resp = str(input("Quer continuar ? {S/N]"))
#     if resp in "Nn":
#         break
# print("-=" * 30)
# print(f"Ao todo, você cadastrou {len(princ)} pessoas.")
# print(f"O maior peso foi de {mai} kg. peso de ", end="")
# for p in princ:
#     if p[1] == mai:
#         print(f" [{p[0]}]", end="")
# print()
# print(f"O menor peso foi de {men}kg. peso de ", end="")
# for p in princ:
#     if p[1] == men:
#         print(f"[{p[0]}]", end="")
# print()
