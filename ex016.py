#CRIE UM PROGRAGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TELCLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
# import math
#
# num = float(input("Digite um número qualquer:"))
# print("O número :{} tem a parte inteira: {}".format(num, math.floor(num)))

# OUTRA FORMA DE FAZER É ELIMINANDO A FUNÇÃO MATH E DEIXANDO APENAS ALGO ESPECIFICO DA BIBLIOTECA

 # from math import trunc
 # num  =  float(input("Digite um valor:"))
 # print("O valor digitado foi {} e a sua porção inteira é : {}".format(num, trunc(num)))


 #OUTRA MANDEIRA DE FAZER SEM RPECISAR IMPORTAR MODO

num = float(input("Digite um valor:"))
print("O valor digitado foi {} e a sua porção inteira é{}".format(num, int(num)))


