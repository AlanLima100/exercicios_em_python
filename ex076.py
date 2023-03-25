#CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA. NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.
lista = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.90,
         "Estojo", 25.00,
         "Transferidor", 4.20,
         "Compasso", 9.99,
         "Mochila", 120.32,
         "Canetas", 22.30,
         "Livro", 34.90)
print("---" * 25)
print("LISTAGEM DE PREÇOS".center(80))
print(f"{lista[0].center(1)}{('...'*21).center(1)}R${lista[1]}\n"
    f"{lista[2].center(1)}{('...'* 20).center(1)} R${lista[3]}\n"
    f"{lista[4].center(1)}{('...'*20).center(1)} R${lista[5]}\n"
    f"{lista[6].center(1)}{('...' * 21).center(1)}R${lista[7]}\n"
    f"{lista[8].center(1)}{('...' * 19).center(1)}R${lista[9]}\n"
    f"{lista[10].center(1)}{('...'* 20).center(1)}R${lista[11]}\n"
    f"{lista[12].center(1)}{('...'* 20).center(1)} R${lista[13]}\n"
    f"{lista[14].center(1)}{('...'* 20).center(1)} R${lista[15]}\n"
    f"{lista[16].center(1)}{('...'* 21).center(1)}R${lista[17]}\n")

#COMO O PROFESSOR FEZ:
listagem = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.90,
         "Estojo", 25.00,
         "Transferidor", 4.20,
         "Compasso", 9.99,
         "Mochila", 120.32,
         "Canetas", 22.30,
         "Livro", 34.90)
print("---" * 20)
print(f"{'LISTAGEM DE PREÇOS':^60}")
print("---" * 20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("---" * 20)
