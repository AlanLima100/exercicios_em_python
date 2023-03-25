# teste = list ( )
# teste.append ("Gustavo")
# teste.append(40)
# galera  = list ( )
# galera.append(teste[:]) # criando uma ligação entre as estruturas, pra que isso não aconteça cria-se uma cópia usando " [:] "
# teste[0] = "Maria"
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# vai mostrar:
# [['Gustavo', 40], ['Maria', 22]]

# galera = [["joão", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# print(galera)
#
# VAI MOSTRAR:
#
# [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# galera = [["joão", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# print(galera[0][0])
#
# VAI MOSTRAR:  joão

galera = [["joão", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(galera[2][1])

# VAI MOSTRAR:  13

# galera = [["joão", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# for p in galera:
#     print(p)
# VAI MOSTRAR:
# ['joão', 19]
# ['Ana', 33]
# ['Joaquim', 13]
# ['Maria', 45]

# galera = [["joão", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# for p in galera:
#     print(p[0]) # vai mostrar só os nome da lista
# joão
# Ana
# Joaquim
# Maria
#
#
# galera = [["joão", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# for p in galera:
#     print(p[1]) # vai mostrar só a idade
# 19
# 33
# 13
# 45


# galera = [["joão", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# for p in galera:
#     print(f"{p[0]} tem {p[1]} anos de idade.")
# joão tem 19 anos de idade.
# Ana tem 33 anos de idade.
# Joaquim tem 13 anos de idade.
# Maria tem 45 anos de idade.

# galera = []
# dado = list()
# for c in range(0, 3):
#     dado.append(str(input("Nome:")))
#     dado.append(int(input("idade:")))
#     galera.append(dado[]) # tira uma cópia de dado " [:]
#     dado.clear() # vai excluir tudo dentro de dado
#
# print(galera) # vai msotrar nome e idade das pessoas que foram colocadas


# galera = []
# dado = list()
# mai = men = 0
# for c in range(0, 3):
#     dado.append(str(input("Nome:")))
#     dado.append(int(input("idade:")))
#     galera.append(dado[:]) # tira uma cópia de dado " [:]
#     dado.clear() # vai excluir tudo dentro de dado
#
# for p in galera:
#     if p[1] >= 21: # pegando a cada lupe do for dentro de galera posição 1 que é a idade, e perguntando se idade é maior que 21 me mostre se não for mostre outra  coisa
#         print(f"{p[0]} é maior de idade.")
#         mai = mai + 1
#     else:
#         print(f"{p[0]} é menor de idade.")
#         men = men + 1
# print(f"Temos {mai} maiores e {men} menores de idade.")




