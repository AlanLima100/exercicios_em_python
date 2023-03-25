#CRIE UM PROGRMA QUE VAI LER VÁRIOS NÚMERO E COLOCAR EM UMA LISTA. DEPOIS DISSO, MOSTRE:
# A) QUANTOS NÚMEROS FORAM DIGITADOS.
# B) A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE.
# C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA.
lista = []
cont = 0
while True:
    lista.append(int(input("Digite um número:")))
    cont = cont + 1
    n = str(input("Quer continuar? [S/N]?")).strip().upper()
    while n not in "sSnN":
        n = str(input("Valor inválido! Quer continuar? [S/N]?")).strip().upper()
    if n == "N":
        break
lista.sort(reverse=True)
print(f"Foram digitados \033[35m{cont}\033[m elementos ")
print(f"Os valores em ordem decrescente são \033[32m{lista}\033[m")
if 5 in lista:
    print(f"O valor \033[31m5\033[m está dentro da lista")
else:
    print("Não existe nenhum número 5 na lista")

#COMO O PROFESSOR FEZ:
valores = []
while True:
    valores.append(int(input("Digite um valor:")))
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break
print("=-" * 30)
print(f"você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
