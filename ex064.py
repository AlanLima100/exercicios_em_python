#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999. QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS
#FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES ( DESCONSIDERANDO O FLAG "999").'
cont = 0
soma = 0
num = 0
total = 0
num1 = 0
f = 0

while num != 999:
    print("Digite: 999 para parar!")
    num = int(input("Digite um número:"))
    soma = num
    soma = num + soma
    cont = cont + 1
    total = total + num

    if num == 999:
        f = total - 999
        print("Você digitou {} números ".format(cont - 1))
        print("A soma entre eles foi de {}".format(f))


#OUTRA FORMA DE FAZER PROFESSOR:

num = cont = soma = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]"))
    soma = soma + num
    cont = cont + 1
print("Você digitou {} número e a soma entre ees foi {} ".format(cont - 1, soma - 999))




num = cont = soma = 0
num = int(input("Digite um número [999 para parar]"))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input("Digite um número [999 para parar]"))
print("Você digitou {} número e a soma entre ees foi {} ".format(cont, soma))
