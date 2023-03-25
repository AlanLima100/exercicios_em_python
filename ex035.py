#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.

a = float(input("Digite o valor da primeira reta:"))
b = float(input("Digite o valor da segunda reta:"))
c = float(input("Digite o valor da terceira reta:"))

if a + b > c:
    print("O valor da reta : {} com a reta : {} mais a reta: {}  FORMAM UM TRIANGULO!!".format(a,b,c))
else:
    print("O valor da reta : {} com a reta : {} mais a reta :{} NÃO FORMAM UM TRIANGULO!!".format(a,b,c))

#MODO QUE O PROFESSOR FEZ

# print("-="*20)
# print("Analisador de Triângulos")
# print("-="*20)
# r1 = float(input("primeiro segmento: "))
# r2 = float(input("segundo segmento: "))
# r3 = float(input("terceiro segmento: "))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print("\033[32mOs segmentos acima formam um trinângulo!")
# else:
#     print("\033[31mOs segmentos A CIMA não Podem formar um triângulo!")

