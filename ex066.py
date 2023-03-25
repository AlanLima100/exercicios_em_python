#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999. QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS
#FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES ( DESCONSIDERANDO O FLAG "999").'
soma = 0
cont = 0
while True:
    print("Digite: 999 para parar!")
    num = int(input("Digite um número:"))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f" A soma dos {cont} valores foi {soma}!")