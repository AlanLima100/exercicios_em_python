#FAÇA UM PROGRMAA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.

# n = int(input("Digite um número:"))
# primo = n / 1
# primo1 = n / n
#
# if primo == n and primo1 == 1:
#     print("O número {} é um número Primo".format(n))
# else:
#     print("{} não é um número PRIMO".format(n))

n = int(input("Digite um número:"))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[33m", end=" ")
        tot = tot + 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[mO número {} foi divisível {} vezes".format(n, tot))
if tot == 2:
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")
