#DESEMVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
# A) QUANTAS VEZES APARECE O VALOR 9
# B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
# C) QUAIS FORAM OS NÚMEROS PARES

n1 = int(input("Digite um número:"))
n2 = int(input("Digite mais um número:"))
n3 = int(input("Digite outro número:"))
n4 = int(input("Digite o último número:"))

n = (n1, n2, n3, n4)
cont = 0
print(f"O número 9 apareceu(ram) {n.count(9)} vez(es)")

if n1 == 3 or n2 == 3 or n3 == 3 or n4 == 3:
    print(f"O número 3 apareceu {n.count(3)} vez(es) e está na posição {n.index(3)+1}°")
else:
    print("O número 3 não apareceu em nenhum momento")

print("Os números pares foram: ", end="")
if n1 % 2 == 0:
    print(n1)
if n2 % 2 == 0:
    print(n2)
if n3 % 2 == 0:
    print(n3)
if n4 % 2 == 0:
    print(n4)


#COMO O PROFESSOR FEZ:

n = (int(input("Digite um número:")),
 int(input("Digite mais um número:")),
 int(input("Digite outro número:")),
 int(input("Digite o último número:")))
print(f"Você digitou os valores {n}")
print(f"O valor 9 apareceu {n.count(9)} vezes")
if 3 in n: # se o 3 estiver dentro da tupla ai mostre ↓
    print(f"O valor 3 apareceu na {n.index(3)+1}° posição")
else:# se não ↓
    print("O valor 3 não foi digitado não foi digitado em nenhuma posição")
print("Os valores pares digitados foram", end=" ")
for m in n: #ESTOU FALANDO AQUI: "PARA CADA NÚMERO PARA CADA VALOR ("n") vá para  ("M")
    if m % 2 == 0: #EXISTE ALGUM NÚMERO DIVISIVEL POR 2 DENTRO DE "M" JÁ QUE EU DISSE NO FOR QUE TODO EM "N" VÁ PARA "M" DE MARIA.
        print(m, end=" ")

