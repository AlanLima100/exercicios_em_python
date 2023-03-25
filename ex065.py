# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMERO INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA
# DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.
num = 0
cont = 0
c = 0
total = 0
h = 0
soma = 1
maior = 1
menor = 0
while c != "N" and c != "n" and h != "N":

    num = float(input("Digite um  número:").strip())
    h = str(input("Quer continuar [S/N]?")).upper().strip()[0]
    soma = num
    cont = cont + 1
    soma = num + soma
    total = total + num
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    while h not in "Ss" and h not in "Nn":
        h = str(input("Valor invalido, quer continuar [S/N]?:"))
media = total / cont
print("O maior foi {}".format(maior))
print("O menor foi {}".format(menor))
print("A soma de todos os números foi de {}!".format(total))
print("Voce digitou {} números e a média foi {}".format(cont, media))


#COMO O PROFESOR FEZ:

resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss": #enquanto minha resposta estiver em "Ss" ( s maiusculo ou minusculo)
    num = int(input("Digite um número:")) #vou ler um número
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N]").upper().strip()[0])
media = soma / quant
print("Você digitou {} números e a média foi {}".format(quant, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))