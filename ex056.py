#DESENVOLVA UM PROGTRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE: - A MÉDIA DE IDADE DO GRUPO - QUAL É O NOME DO HOMEM MAIS VELHO. - QUANTAS MULHERES
# TÊM MENOS DE 20 ANOS.
maiorIDADE = 0
menorIDADE = 0
maisvelho = 0
mulhermenosde20 = 0
for c in range(1, 5):
    nome = str(input("Qual é o seu nome?:"))
    idade = int(input("Qual é sua idade?:"))
    print("""
    [0]Feminino
    [1]Masculino
    [2}Outros""")
    sexo = int(input("Qual o seu sexo?:"))
    itens = ("Feminino", "Masculino", "Outros")
    if c == 1:
        idade1 = idade
    if c == 2:
        idade2 = idade
    if c == 3:
        idade3 = idade
    if c == 4:
        idade4 = idade
    if c == 1 and sexo == 1:
        maiorIDADE = idade
        maisvelho = nome
    if sexo == 1 and idade > maiorIDADE:
        maiorIDADE = idade
        maisvelho = nome
    if sexo == 0 and idade < 20:
        mulhermenosde20 = mulhermenosde20 + 1
    else:
        if idade > maiorIDADE:
            maiorIDADE = idade
        if idade < menorIDADE:
            menorIDADE = idade
    if maiorIDADE == idade:
        maisvelho = nome
media = ((idade1 + idade2 + idade3 + idade4) / 4)
print("A media do grupo é de {} anos".format(media))
print(("O homem mais velho do grupo tem {} anos de idade e se chama {} ".format(maiorIDADE, maisvelho)))
print("Ao todo são {} mulheres abaixo dos 20 anos".format(mulhermenosde20))



# maiorIDADE = 0
# somaidade = 0
# mulheremenosde20 = 0
# maisvelho = 0
# media1 = 0
#
# for c in range(1, 5):
#
#     nome = str(input("Qual é o seu nome?:")).strip().upper()
#     idade = int(input("Qual é sua idade?:"))
#     sexo = str(input("Qual o seu sexo[M/F]?:").upper().strip())
#     somaidade += idade
#     if c == 1 and sexo in "Mm":
#         maiorIDADE = idade
#         maisvelho = nome
#     if sexo in "Mm" and idade > maiorIDADE:
#         maiorIDADE = idade
#         maisvelho = nome
#     if sexo in "F" and idade < 20:
#         mulheremenosde20 += 1
# media1 = somaidade / 4
# print("A media do grupo é de {} anos".format(media1))
# print(("O homem mais velho do grupo tem {} anos de idade e se chama {}".format(maiorIDADE, maisvelho)))
# print("Ao todo são {} mulheres com menos de 20 anos".format(mulheremenosde20))



#PROFESSOR FEZ ASSIM
# somaidade = 0
# maiorIDADE = 0
# maisVelho = 0
# mulhermenosde20 = 0
#
# for c in range(1, 5):
#
#     nome = str(input("Qual é o seu nome?:")).strip().upper()
#     idade = int(input("Qual é sua idade?:"))
#     sexo = str(input("Qual é o seu sexo [M/F]:")).strip().upper()
#     somaidade = somaidade + idade
#     if c == 1 and sexo in "Mm":
#         maiorIDADE = idade
#         maisVelho = nome
#     if sexo in "Mm" and idade > maiorIDADE:
#         maiorIDADE = idade
#         maisVelho = nome
#     if sexo in "Ff" and idade < 20:
#         mulhermenosde20 = mulhermenosde20 + 1
#
#
# media = somaidade / 4
# print(" A media do grupo é {} anos".format(media))
# print("O homem mais velho tem {} anos e se chama {}".format(maiorIDADE, maisVelho))
# print("Ao todo são {} mulheres com menos de 20 anos de idade".format(mulhermenosde20))