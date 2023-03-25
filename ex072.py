#CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE. SEU PROGRAMA DEVERÁ LER UM NÚMERO PEO TECLADO (ENTRE 0 E 20) E MOSTRÁ - LO
# POR EXTENSO.

# cont = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito","Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
#
# while True:
#     num = int(input("Digite um número entre 0 e 20:"))
#     if num <= 20 and num >= 0:
#         break
#     else:
#         print("Tente novamente...", end="")
# print(f"Você digitou o número {cont[num]}")
import numbers

cont = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito","Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um número entre 0 e 20:"))
    if num <= 20 and num >= 0:
        print(f"Você digitou o número \033[34m{cont[num]}\033[m")
        c = str(input("Quer continuar [S/N}?:").upper().strip())
        while c not in "SN":
            c = str(input("Valor invalido! Quer continuar [S/N]?:").upper().strip())
        if c == "N":
            break
    else:
        print("Tente novamente...", end="")
print("\033[32mAté breve!")

