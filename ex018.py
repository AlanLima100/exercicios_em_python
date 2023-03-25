#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E A TANGETE DESSE ÂNGULO
# import math
#
# angulo = float(input(" Qual é o valor do angulo:"))
#
# seno = cateto_oposto / hipotenusa
# cosseno = cateto_adjacente / hipotenusa
# tangente = cateto_oposto / cateto_adjacente
#
# hp = math.sqrt()
# print("O valor do Seno de {} é: {}")
# print("O valor do Coseno de {} é {}")
# print("O valor da tangente de {] é :{}")

#UMA FORMA DE FAZER E BUSCANDO DENTRO DA BIBLIOTECA MATH A FUNÇÃO "MATH.SIN" PARA CALCULAR DO SENO bs: dentro do Pycharm a formula de seno e coseno não está em graus sentigrados, ele tem que está
#representado em radiandos e para fazer a conversão: math.sin(math.radians(ângulo)), tô pegando o angulo digitado, convertendo para radiando, vou pegar o  angulo convertido para radiando e calcular o seno dele
# import math
# ângulo = float(input("Digite o ângulo qu você deseja:"))
# seno = math.sin(math.radians(ângulo))
# print('O ânguulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
#
# cosseno = math.cos(math.radians(ângulo))
# print("O ângulo de {} tem o COSSENO de {:.2f}".format(ângulo, cosseno))
#
# tangente = math.tan(math.radians(ângulo))
# print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, tangente))


#SIMPLIFICANDO

from math import radians, sin, cos, tan
ângulo = float(input("Digite o ângulo qu você deseja:"))
seno = sin(radians(ângulo))
print('O ânguulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))

cosseno = cos(radians(ângulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ângulo, cosseno))

tangente = tan(radians(ângulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, tangente))
