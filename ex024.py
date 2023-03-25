# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
#
# cidade = str(input("Qual é o nome da sua cidade?:")).strip()
# print(cidade[:5].upper() =="SANTO")
#
# # Outra forma de fazer melhorada, posi idependente de letras maisuculas ou mninusculas.

cidade = str(input("Em que cidade você nasceu?").strip())
print(cidade[:5].upper() == "SANTO")  #TRANSFORMOU TUDO QUE O USUSARIO DIGITAR EM MAIUSCULO SE FOR A PALAVRA "SANTO" DARÁ VERDADEIRO TRUE
