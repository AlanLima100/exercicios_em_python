#CRIE UM PROGRAMA QUE CRIE O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
import datetime
cont = 0
for c in range(1, 8):
    ano = int(input("Em que ano a {}°pessoa nasceu?:".format(cont + 1)))
    idade = datetime.date.today().year - ano
    cont = cont + 1
    if idade >= 18:
        maior = c
    else:
        menor = c - maior
print("\033[36mAo todo tivemos {} pessoas maiores de idade \033[m".format(maior))
print("\033[31mE também tivemos {} pessoas menores de idade".format(menor))

#
# #PROFESSOR FEZ:
#
# from datetime import date
# atual = date.today().year
# totmaior = 0
# totmenor = 0
# for pess in range(1, 8):
#     nasc = int(input("Em que ano {}ª pessoa nasceu?".format(pess)))
#     idade = atual - nasc
#     if idade >= 21:
#         totmaior += 1
#         totmenor += 1
# print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
# print(("E Também tivemos {} pessoas menores de idade".format(totmenor)))


#OUTRA FORMA DE FAZER DO YOUTUBE
# from datetime import date
# contmenor = 0
# contmaior = 0
# anohj = date.today().year
# for contagem in range(1, 8):
#     ano = int(input(f'Digite o ano de nascimento da {contagem}° pessoa: '))
#     if anohj - ano >= 18:
#         contmaior += 1
#     else:
#         contmenor += 1
# print(f'Há um total de {contmaior} pessoas maiores de idade e {contmenor} pessoas menores de idade.')
