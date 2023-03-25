#CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL, MOSTRE:
# A) QUAL É O TOTAL FASTO NA COMPRA.
# B) QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000,00
# C) QUAL É O NOME DO PRODUTO MAIS BARATO
logo = ("LOJA SUPER PREÇO BAIXO")
c = p = cont = soma = preco = menor = j = 0
while True:
    print("=-" * 25)
    print(f"{logo.center(50)}")
    print("=-" * 25)
    produto = str(input("Nome do Produto:").strip().upper())
    preco = float(input("Preço R$:").strip())
    preco = preco
    cont = cont + 1
    soma = soma + preco
    if cont == 1:
        menor = preco
        j = produto
    elif preco < menor:
        menor = preco
        if menor == preco:
            j = produto
    c = str(input("Quer continuar? [S/N] :").upper().strip())
    if preco > 1000:
        p = p + 1
    while c not in "S" and c not in "N":
        c = str(input("Valor invalido!, Quer continunar? [S/N] :").upper().strip())
    if c == "N":
        break
print("=-" * 25)
f = ("FIM DO PROGRAMA")
print(f"{f.center(50)}")
print("=-" * 25)
print(f"\033[32mO total da compra foi de R${soma:.2f}")
print(f"Temos \033[34m {p} \033[m \033[32mproduto(os) custando mais de R$1000,00")
print(f"\033[36mO produto mais barato foi \033[31m{j}\033[m \033[36mque custa R${menor:.2f}")

#COMO O PROFESSOR FEZ:
# total = totmil = menor = cont = 0
# barato = " "
# while True:
#     produto = str(input("Nome do Produto: "))
#     preço = float(input("Preço: R$"))
#     cont += 1
#     total += preço
#     if preço > 1000:
#         totmil += 1
#     if cont == 1 or preço < menor:
#         menor = preço
#         barato = produto
#     resp = " "
#     while resp not in "SN":
#         resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
#     if resp == "N":
#         break
# print(f" FIM DO PROGRAMA".center(50))
# print(f"O total da compra foi de R${total:.2f}")
# print(f"Temos {totmil} produtos custando mais de R$1000.00")
# print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")