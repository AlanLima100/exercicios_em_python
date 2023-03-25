#FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOA. NO FINAL, MOSTRE QUEAL FOI O MAIOR E MENOR PESO LIDOS.
# cont = 0
# maior = 0
# menor = 0
# for c in range(1, 6):
#     cont = cont + 1
#     peso = float(input("Qual é o peso da {}° pessoas?:".format(c)))
#
#     if c == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
#
#
# print(("O maior foi {}".format(maior)))
# print("O menor foi {}".format(menor))

#PROFESSOR FEZ:
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {}° pessoa".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(("O maior peso lido foi de {}kg".format(maior)))
print("O menor peso lido foi de {}kg".format(menor))


