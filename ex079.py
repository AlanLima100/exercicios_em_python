#CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADSATRE-OS EM UMA LISTA. CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICONADO. NO FINAL, SERÃO EXIBIDOS
# TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE.
lista = []
while True:
    t = int(input("Digite um número qualquer:"))
    if t not in lista:
        lista.append(t)
        print("Valor adiconado com sucesso...")
    else:
        print("Número já existente, não foi adicionado!")
    s = str(input("Quer continuar? [S/N]:")).strip().upper()

    while s not in "sSnN":
        s = str(input("Valor inválido! Quer continuar? [S/N]:")).strip().upper()
    if s == "N":
        break
lista.sort()
print(f"Os valores digitados foram {lista} ")


#COMO O PROFESSOR

numeros = list()
while True:
    n = int(input("Digite um valor:"))
    if n not in numeros:
        numeros.append(n)
        print("Valor adiconado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    r = str(input("Quer continuar? [S/N]"))
    if r in "Nn":
        break
print("-= "* 30)
numeros.sort()
print(f"Você digitou os valores {numeros}")