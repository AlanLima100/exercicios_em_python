# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATRETO ADJACENTE DE UM TRIÂNGUO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.
import math
cateto_oposto = float(input("Digite o valor do cateto oposto:"))
cateto_adjacente = float(input("Digite o valor do catelo adjacente:"))

hp = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print("O comprimento da hipotenusa é {} cm".format(hp))


#OUTRA FORMA DE FAZER UTILIZANDO A FORMULA PARA CALCULAR A RAIZ QUADRADA
co = float(input("Comprimento do catto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(" A hipotenusa vai medir {:.3f}".format(hi))

#OUTA MANDEIRA DE FAZER É IMPORTANDO DA BIBLIOTECA MATH A FUNÇÃO DE HIPOTENUSA
import math

co = float(input("Comprimento do cateto aposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = math.hypot(co, ca)
print("A hipotenusa vai medir {:.3f}".format(hi))

# OUTA MANDEIRA DE FAZER É IMPORTANDO DA BIBLIOTECA MATH APENAS FUNÇÃO DE HIPOTENUSA UTILIZANDO O "FROM"
# from math import hypot
#
# co = float(input("Comprimento do cateto aposto:"))
# ca = float(input("Comprimento do cateto adjacente:"))
# hi = hypot(co, ca)
# print("A hipotenusa vai medir {:.3f}".format(hi))
