#Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos digitos separados. Ex: digiite um número: 1834. unidade = 4, dezena = 3, centena = 8, milhar = 1

# n1 = input("Digite um número de 0 à 9999:")
# espaco = "0000"
# juncao = espaco + n1
#
# tamanho = len(juncao)
# print("Unidade:", juncao[tamanho-1])
# print("Dezena:", juncao[tamanho-2])
# print("Centeza:", juncao[tamanho-3])
# print("Milhar:", juncao[tamanho-4])

# OUTRA FORMA DE FAZER:

num  =  int(input("Informe um número:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(' Analisando o número {}'.format(num))
print("Unidade: {}".format(u))
print("dezena:{}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
