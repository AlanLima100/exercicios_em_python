#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL.

c = 1
n = int(input("Digite um número:"))
while n != 1:
    c = c * n
    n = n - 1
print(c)




import math
cont = 0
num = int(input("Digite um número:"))
k = math.factorial(num)
print(k)
antecessor = num - 1

while num != k:
    antecessor = num - 1
    num = antecessor + num


print("O fatorial de {} é {}".format(num, num))


#PROFESSOR FEZ ASSIM:

n = int(input("Digite um número para calcular seu fatorial:"))
cont = n
f = 1
print("Calculando{}! = ".format(n), end="")
while cont > 0:
    print(" {}".format(cont), end="")
    print(" x " if cont > 1 else " = ", end="") # bote um  "x" se (if)  cont for maior (>) que 1 se não (else) mostre um "="
    f = f * cont
    cont = cont - 1

print("{} ".format(f))


#USANDO O FOR:

num = int(input("Digite o primeiro termo:"))
r = 1

for r in range(num, 0, -1):
    r = r * num
    print("→ {} →".format(r), end="")







