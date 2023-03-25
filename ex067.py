#FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.

cont = 0
s = 0
soma = 0
total = 0
while True:
    num = int(input("Quer ver a tabuada de qual valor?"))
    if num < 0:
        break
    while cont < 10:
        cont = cont + 1
        soma = num * cont
        total = soma
        print("{} X {} = {}".format(num, cont, total))
    cont = 0

#PROFESSOR USANDO O FOR

cont = 0
s = 0
soma = 0
total = 0
while True:
    num = int(input("Quer ver a tabuada de qual valor?"))
    if num < 0:
        break
    for cont in range(1, 11):
        cont = cont + 1
        soma = num
        soma = num * cont
        total = soma
        print("{} X {} = {}".format(num, cont, total))
        if num == -num:
            break


