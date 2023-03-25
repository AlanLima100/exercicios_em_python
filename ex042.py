#REFAÇA O DESAFIO 035 DOS TRINÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO: - EQUILÁTERO: TODOS OS LADOS IGUAIS - ISÓSCELES: DOIS LDAOS IGUAIS
#- ESCALENO: TODOS OS LADOS DIFERENTES

a = float(input("Digite o valor da primeira reta?:"))
b = float(input("Digite o valor da segunda reta?:"))
c = float(input("Digite o valor da terceira reta?:"))

if a + b > c and b + c > a and a + c > b:
    print("O valor da reta :{}, com a  reta :{} mais a reta: {}, \033[32mFORMAM UM TRIÂNGULO\033[m".format(a, b, c))
    if a == b and a == c and b == c and b == a and c == a and c == b:
        print("Todos os lados são IGUAIS sendo assim \033[32mTRIÂNGULO EQUILÁTERO!!")
    elif a == b or a == c or b == a or b == c or c == a or c == b:
        print("Apenas dois lados são iguais, sendo assim \033[35mTRIÃNGULO ISÓSCELES!!")
    elif a != b and a != c or b != a or b != c or c != a or c != b:
        print("Todos os lados são DIFERENTES, sendo assim \033[36mTRIÂNGULO ESCALENO!!")
else:
    print(" O valor da reta: {}, com a reta: {}, mais a reta: {}, \033[31mNÃO FORMAM UM TRIÃNGULO\033[m".format(a, b, c))

# COMO O PROFESSOR FEZ:

r1 = float(input("Primeiro segmento:"))
r2 = float(input("Segundo segmento:"))
r3 = float(input("terceiro segmento:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")





