# DESAFIO 022 - CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE: O NOME COM TODDAS AS LETRAS MAIUSCULAS - O NOME COM TODAS MINUSCULAS - QUANTAS LETRAS AO
# TODO ( SEM CONSIDERAR ESPAÇOS). QUANTAS LETRSA TEM O PRIEMIRO NOME.

nome = str(input("Infome seu nome completo:"))
print(nome.upper())
print(nome.lower())
dividido = nome.split()
nome1 = " ".join(dividido)
print("Seu nome tem {} caracteres".format(len(nome1)))
print("Seu primeiro nome  tem {} caracteres".format(len(dividido[0])))

# Outra forma de fazer

# nome = str(input("Digite seu nome completo:")).strip()
# print("Analisando seu nome...")
# print("Seu nome em maiusculas é {}".format(nome.upper()))
# print("Seu nome em minusculas é {}".format(nome.lower()))
# print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
# print("Seu primeiro nome tem {} letras".format(nome.find(" ")))





