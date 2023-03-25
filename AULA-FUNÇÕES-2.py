#INTERATICVE

# help() # abre e fecha parenteses é um metodo: vai ajudar a descobrir a funcionalidade das funções.
#
# print("Olá mundo") # se eu não souber pra que serve o "print" ele vai me ajudar a descobrir sua funcionalidade
# help(print)
#
# # OUTRA MANEIRA DE PEDIR AJUDAR:
# print(input.__doc__) # informação sobre a função

#DOCSTRINGS =

# def contador(i, f, p):
#     #meu DOCSTRINGS
#     """
#     → FAZ UMA CONTAGEM E MOSTRA NA TELA
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p:passo da contagem
#     :return:sem retorno
#     função criada por Alan Vitor de João Pessoa-PB
#     """
#     c = i
#     while c <= f:
#         print(f"{c}", end="..")
#         c = c + p
#     print("FIM")
#
#
# contador(2, 10, 2)
# help(contador)
#--------------------------------------------
# PARAMETRO OPCIONAL:

# def somar(a=0, b=0, c=0): # parametro opcional no "somar(8, 4) " não tem o terceiro valor isso dá um erro, com o parametro opcional "c=0" eu to falando que se não tiver um terceiro valor iguale a zero
#     s = a + b + c
#     print(f"A soma vale {s}") # se eu quiser mais de três parametros preciso usar a funcionalizade "*num"
#
#
# somar(3, 2, 5)
# somar(8, 4)
# vai mostrar:

# A soma vale 10
# A soma vale 12
#-----------------------------------------------
#  ESCOPO DE VARIÁVEIS:
#
# def teste():
#     x = 8 # variável LOCAL
#     print(f"na função teste, n vale {n}")
#     print(f"Na função teste, x vale {x}")
#
#
# #programa principal
#
# n = 2 # vaciável GLOBAL
# print(f"No programa principal, n vale {n}")
# teste()
#
# def teste(b): #inicialmente o "teste(b)" vale 5 pois no programa principal eu disse que a = 5 e que o teste(a) logo cria-se uma cópia de a para dentro do parametro teste(b)
#     global a # usando essa funcionalidade o "a" do programa principal passa a valer 8 pois é o 5 mais 4
#     b = b + 4 # aqui eu disse que b era b (5) + 4, logo agora o b vale 9...obs: o valor de a não é alterado
#     c = 2 #
#     print(f"A dentro vale {a}")
#
#
# a = 5 # global
# teste(a)
#
# print(a)
#
# print(teste)
# ------------------------------------------------------------------------
#
# RETORNANDO VALORES
#
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f"A soma vale {s}")
#
#
# somar(3, 2, 5)
#
# vai mostrar:
# A soma vale 10
#
# se eu usar o return
#
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(2, 4)
# r3 = somar(4)
#
# print(f" Os resultados foram {r1}, {r2} e {r3}")
#
# def mostra(nome):
#     return f"*** {nome} ***"
#
#
# nome = "Alan Vitor"
# valor_do_print = mostra(nome)
#
# print(f"Na variável {valor_do_print}")
#
#
#
# def mostra(nome):
#     novo = "*** "
#     novo = novo + nome
#     novo = novo + ' ***'
#     return novo
#
#
#
# valor_do_print = mostra("Alan Vitor")
# print(f"Na variável {valor_do_print}")
#
#
# valor_do_print = mostra("Arthur Venicius")
# print(f"Na variável {valor_do_print}")
#
#
#
#
#
#
#
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# print(somar(3, 2, 5))
# r2 = somar(2, 4)
# r3 = somar(4)
#
# print(f" Os resultados foram , {r2} e {r3}")
#
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f = f * c
#
#     return f
#
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
#
# n = int(input("Digite um número: "))
# print(f"O fatorial de {n} é igual a {f1} > {f2}  > {f3}")
# print(f"O fatorial de {n} é igual a {fatorial(n)}")
#
#
#
#
# for c in range(5, 0, -1):
#     print(f"{c} tome")
#
#
#

# def contador(i, f, p):
#     #DOCSTRINGS →→→→→→→→→→→→→→→→→→→→→→→→ DOCSTRINGS
#     """
#
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f"{c} ", end= '')
#         c = c + p
#
#
# contador(2, 100, 10)
def dobra(lst):
    pos = 0
    print(f"{lst[pos]} >>>")
    while pos < len(lst):
        print(f"{lst[pos]} >>>")
        lst[pos] = lst[pos] * 2
        pos = pos + 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

def soma(* valores):
    print(f"{valores} >>>")
    s = 0
    for num in valores:
        print(f"{num}>>>>>>>><<<<<@")
        s = s + num
    print( f" Somando os valores {valores}  temos {s}")


soma(5, 2)
soma(2, 9, 4)




























