#Refaça p DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.
#DESENVOVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA pa. nO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

num = int(input("Digite o primeiro termo:"))
razão = int(input("Digite a razão:"))
cont = 0
r = num
while cont <= 10:
    print(" {} -".format(r),end="") # "r" tá recebendo o primeiro termo que chamei de "num", logo r = 2 + 5, so fiz substituir r = 5 e razão = 5 se eu pôr, então o contator vai contar até
    r = r + razão                   # for igual a 10 e parar.

    cont = cont + 1


#PROFESSOR FEZ:

num = int(input("Qual é o valor do primeiro termo?:"))
razão = int(input("Qual é o valor da razão?:"))
cont = 1
g = num
while cont <= 10:
    print(" {} → ".format(g), end="")
    g = g + razão
    cont = cont + 1
print("Pausa")




#OUTRA FORMA DE FAZER COM WHILE


num = int(input("Digite o primeiro termo:"))
r = int(input("Digite sua razão:"))
cont = 1
t = num
mais = 10
novotermo = 0

while mais != 0:
    novotermo = novotermo + mais
    while cont <= novotermo:
        print("{} → ".format(t), end="")
        t = t + r
        cont = cont + 1
    print("Pausa")
    mais = int(input("Quantos termos quer adicionar?:"))
print("Temos ao todo {} ".format(novotermo))
