# VARIÁVIS COMPOSTAS (DICIONÁRIOS)

# estado = dict ( )
# brasil =  list ( )
#
# for c in range ( 0, 3):  # de 0 até 3
#        estado ["uf" ] = str( input ("unidade Federativa: ") )
#        estado ["sigla" ] = str( input ("sigla do estado: ") )
#        brasil.append(estado.copy ( ) ) # estou tirando um cópia de estado e adicioando em brasil, em dicionãdio não se usa [:]
# print( brasil )
#                              #vai mostrar # [{'uf': 'paraiba', 'sigla': 'pb'}, {'uf': 'Natal', 'sigla': 'RN'}, {'uf': 'Sergipe', 'sigla': 'SE'}]
#


#obs se eu quiser pôr em ordem é só fazer com um FOR

# estado = dict()
# brasil = list()
#
# for c in range(0, 3):  # de 0 até 3
#     estado["uf"] = str(input("unidade Federativa: "))
#     estado["sigla"] = str(input("sigla do estado: "))
#     brasil.append(estado.copy())# estou tirando um cópia de estado e adicioando em brasil, em dicionãdio não se usa [:]
# for e in brasil:# para cada estado em brasil
#     for k, v in e.items():
#         print(f"O campo { k } tem valor { v }.\n" )



# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado["uf"] = str(input("unidade Federativa: "))
#     estado["sigla"] = str(input("sigla do estado: "))
#     brasil.append(estado.copy())# estou tirando um cópia de estado e adicioando em brasil, em dicionãdio não se usa [:]
# for e in brasil:
#     for v in e.values():
#         print(v, end=" ")
#     print()


# filme = {"Titulo": "Star Wars", "Ano": 1977, "diretor": "George Lucas"} # chaeves ou keys, valor, chave e item
#
# print(filme.values()) # vai mostrar → dict_values(['Star Wars', 1977, 'George Lucas']) TODOS OS VALORES
# print(filme.keys()) # Vai mostrar → dict_keys(['Titulo', 'Ano', 'diretor']) TODAS AS CHAVES
# print(filme.items()) # vai me mostrar → tanto os valores quando as chaves → dict_items([('Titulo', 'Star Wars'), ('Ano', 1977), ('diretor', 'George Lucas')])
# print()
# print()
# for k, v in filme.items():
#     print(f"O {k} é {v}")
#     # vai mostrar :
#     # O Titulo é Star Wars
#     # O Ano é 1977
#     # O diretor é George Lucas

# locadora = list()
# biblioteca1 = {"Titulo": "Star Wars", "Ano": 1977, "diretor": "Gerorge Lucas"}
# biblioteca2 = {"Titulo": "Avengers", "Ano": 2012, "diretor": "joss Whedon"}
# biblioteca3 = {"Titulo": "Matrix", "Ano": 1999, "diretor": "Wachowski"}
#
# locadora.append(biblioteca1)
# locadora.append(biblioteca2)
# locadora.append(biblioteca3)
# print(locadora[0]["Ano"])

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado["uf"] = str(input("Unidade Federativa: "))
#     estado["sigla"] = str(input("Sigla do Estado: "))
#     brasil.append(estado.copy())
# print(brasil)

#resultado
#[{'uf': 'Paraíba', 'sigla': 'PB'}, {'uf': 'Natal', 'sigla': 'RN'}, {'uf': 'Sergipe', 'sigla': 'Se'}]

estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1")
    # print(e)
# {'uf': 'Paraíba', 'sigla': 'PB'}
# {'uf': 'Natal', 'sigla': 'RN'}
# {'uf': 'Sergipe', 'sigla': 'SE'}
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2")
    for k, v in e.items():
        # print(f"O campo {k} tem valor {v}")
    # O campo uf tem valor Paraíba
    # O campo sigla tem valor PB
    # O campo uf tem valor Natal
    # O campo sigla tem valor RN
    # O campo uf tem valor Sergipe
    # O campo sigla tem valor SE
        #print(v)
        # Paraíba
        # PB
        # Natal
        # RN
        # Sergipe
        # SE
        print(v, end=" ")
    print()
        # ParAIBA PB
    # Natal RN
    # Sergipe SE








