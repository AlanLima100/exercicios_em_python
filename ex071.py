#CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO) E O PROGRAMA VAI FUNCIONAR QUANTAS
#CÉDULAS DE CADSA VALOR SERÃO ENTREGUES. OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE r$ 50, r$ 20, R$ 10  E R$ 1

lista = [100, 50, 20, 10, 5, 2, 1]
valor = int(input('Insira o valor que desaja sacar R$ '))
cont = 0
while True:
    if valor >= lista[cont]:
        nota = valor // lista[cont]
        print(nota)
        print(f'Total de {nota} nota(as) de R$ {lista[cont]}')
        valor = valor % lista[cont]
    cont += 1
    if valor == 0:
        break
print('\nVolte sempre ao Banco do CEV! Tenha um bom dia!')


# COMO O PROFESOR FEZ:
# print("=-" * 30)
# print("BANCO CEV".center(50))
# print("=-" * 30)
# valor = int(input("Que valor você quer sacar? R$"))
# total = valor
# ced = 50
# totced = 0
# while True:
#     if total >= ced:
#         total = total - ced
#         totced = totced + 1
#     else:
#         if totced > 0:
#             print(f"Total de {totced} cédulas de R${ced}")
#         if ced == 50:
#             ced = 20
#         if ced == 20:
#             ced = 10
#         if ced == 10:
#             ced = 1
#         if total == 0:
#             break
# print("=0" * 30)
# print("Volte sempre ao BANCO CEV! Tenha um bo dia!")
#
#
#
# # mais uma vez:
# valor = int(input("Qual o valor do saque?R$:"))
# total = valor
# cedula = 50
# cont = 0
#
# while True:
#     if total >= cedula:
#         total = total - cedula
#         cont = cont + 1
#     else:
#         if cont > 0:
#             print(f"Ao todo são {cont} cédula(as) de R${cedula} ")
#         if cedula == 50:
#             cedula = 20
#         if cedula == 20:
#             celula = 10
#         if cedula == 10:
#             cedula = 1
#         cont = 0
#         if total == 0:
#             break
# print("=-" * 30)
# print("volte sempre ao BRANCO CEV ! Tenha um bom dia!")
#
#




















