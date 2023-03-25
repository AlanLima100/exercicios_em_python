#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR IMPAR, DESCONSIDERE-O.
soma = 0
cont = 0
for num in range(1, 7):
    num = int(input('Digite {}° número:'.format(num)))
    if num % 2 == 0:
        soma = cont + num

print("A soma dos núemros pares são {}".format(soma))

