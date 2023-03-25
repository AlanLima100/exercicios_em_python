#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

n1 = float(input("Digite o seu primeiro número:"))
n2 = float(input("digite o seu segundo número:"))
n3 = float(input("Digite o seu terceiro número:"))



if n1 > n2:
    print("O número {} é maior que o número {}".format(n1, n2))
else:
    print("O número {} é menor que o número {}".format(n1, n2))

if n1 > n3:
    print(" O número {} é maior que {}".format(n1, n3))
else:
    print("O número {} é MENOR que o número {}".format(n1, n3))

if n2 > n1:
    print("O número {} é maior que o número {}".format(n2, n1))
else:
    print("O numero {} é MENOR que o número {}".format(n2, n1))

if n2 > n3:
    print(" O número {} é maior que o número {}".format(n2, n3))
else:
    print("O numero {} é MENOR  que o número {}".format(n2, n3))

if n3 > n1:
    print("O número {} é maior que o número {}".format(n3,n1))
else:
    print("O número {} é MENOR que o número {}".format(n3, n1))

if n3 > n2:
    print(" O número {} é maior que o número {}".format(n3, n2))
else:
    print("O número {} é MENOR que o número {}".format(n3,n2))


##### PODE SER FEITO ASSIM TBM


a = float(input("Digite o seu primeiro número:"))
b = float(input("digite o seu segundo número:"))
c = float(input("Digite o seu terceiro número:"))
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c

#OUTRA FORMA DE FAZER COM O PROFESSOR:
a = int(input("Primeiro valor:"))
b = int(input("Segundo valor:"))
c = int(input("Terceiro valor:"))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O maior valor digitado foi {}".format(maior))

print("O menor valor digitado foi {}".format(menor))

