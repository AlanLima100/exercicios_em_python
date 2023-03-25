# #CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT() ). NO FINAL
#MOSTRE A LISTA ORDENADA NA TELA.
lista = []
for cont in range(1, 6):
    num = int(input(f"Digite o {cont}° valor númerico: "))
    if cont == 1 or num >= lista[-1]:
        lista.append(num) # adicionando o num no final da fila na lista
    elif num <= lista[0]:
        lista.insert(0, num)
    elif lista[0] <= num <= lista[1]:
        lista.insert(1, num)
    elif lista[1] <= num <= lista[2]:
        lista.insert(2, num)
    elif lista[2] <= num <= lista[3]:
        lista.insert(3, num)

print(lista)

# lista = [3, 2, 5, 6, 9]
# for cont in range(1, 6):
#     num = int(input("Digite um valor:"))
# lista.append(lista)# adicionando o num no final da fila na lista
# lista.insert(1, 3) # adiciona o 3 na posição 1 e os demais vão para posição seguinte
# print(lista)
# lista = []


#COMO O PROFESSOR FEZ:
lista = []
for c in range(0, 5):
    n = int(input("Digite um valor:"))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos = pos + 1
print("-=" * 30)
print(f"Os valores digitados em ordem foram {lista}")

