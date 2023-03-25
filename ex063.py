# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUêNCIA DE FIBONACCI.
print("=-="* 20)
print("Sequência de Fibonacci")
print("=-="* 20)
num = int(input("Quantos termos voce quer?:"))
cont = 0
atual = 0
proximo = 1
soma = 1

while cont <= num:
    print(f" → {atual} ", end="")
    cont = cont + 1
    soma = atual + proximo
    atual = proximo
    proximo = soma




















# num = int(input("Quantos termos você quer mostrar?:"))
# cont = 0
# soma = 1
# proximo = 1
# anterior = 0
#
# while cont <= num:
#     print("{} →".format(anterior), end="")
#     cont = cont + 1
#     soma = proximo + anterior
#     anterior = proximo
#     proximo = soma
# print("Fim")


#PROFESOR FEZ ASSIM:

# print("=-="* 20)
# print("Sequência de Fibonacci")
# print("=-="* 20)
#
# num = int(input("Quantos termos você quer mostrar?:"))
# t1 = 0
# t2 = 1
# cont = 3
# print("{} → {} →".format(t1, t2), end="")
# while cont <= num:
#     t3 = t1 + t2
#     print(" {} →  ".format(t3), end="")
#     t1 = t2
#     t2 = t3
#     cont = cont + 1
#
#
#
#
# print(" → FIM")