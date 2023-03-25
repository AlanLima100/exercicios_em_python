#DESENVOVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA pa. nO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

num = int(input("Primeiro termo:"))
r = int(input("Razão:"))
decimo = num + (11 - 1) * r
for razão in range(num, decimo, r):
    print(razão)

# professor
# num = int(input("Priemiro termo:"))
# r = int(input("Ração:"))
# decimo = num + (10 - 1) * r
# for razão in range(num,decimo + r,r):
#     print(razão)
