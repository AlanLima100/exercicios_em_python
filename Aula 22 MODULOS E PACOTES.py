# def fatorial(n):
#     f = 1
#     for c in range(num, 0, -1):
#         f = f * c
#     return f
#
#
# num = int(input("Digite um valor: "))
# fat = fatorial(num)
# print(f"O fatorial de {num} é {fat}")
import uteis

num = int(input("Digite um valor: "))
fat = uteis.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {uteis.dobro(num)}")
