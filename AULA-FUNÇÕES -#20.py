def mostralinha(): # função
    print("_" * 30)


mostralinha()
print(" SISTEMA DE ALUNOS")
mostralinha()
mostralinha()
print(" CADASTRO DE FUNCIONÁRIOS")
mostralinha()
mostralinha()

#------------------------------------------
#def mensagem(msg):  # dentro pode ser qualquer coisa.
# ------------------------------------------

# def título(txt):
#     print("-" * 30)
#     print(txt)
#     print("-" * 30)
#
#
# título(" CURSO EM VÍDEO ") # pegando o " curso em vídeo" jogando para dentro de "txt"
# título(" APRENDA PYTHON") # o conteúdo está atrelado ao "txt" dentro de título
# título(" ALAN VITOR CÂNDIDO ")

# --------------------------------
# def soma(a, b):
#     print(f" A = {a}  e B = {b}")
#     s = a + b
#     print(f" A soma A + B = {s}")
#
#
# soma(b=4, a=5) # vai me mostrar a soma mesmo mudando a ordem de procedência
# soma(4, 5)
# soma(3, 9, 5) # neste caso não vai somar por que eu defini que "def soma" recebe apenas dois valores, como passei três dá erro.

# --------------------------------
# EMPACOTAMENTO
# def contador(*num): # neste caso eu botei o "*"( desempacotar) e o "num"( parametro), pegando tudo e jogando dentro de "num"
#     for valor in num: # para cada valor em "num"
#         print(num) # criou um tupla e fez a soma de todos os valores
#
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

#resultado: criou varias tuplas
# (2, 1, 7)
# (8, 0)
# (4, 4, 7, 6, 2)


# --------------------------------
# def contador(*num): # neste caso eu botei o "*"( desempacotar) e o "num"( parametro), pegando tudo e jogando dentro de "num"
#     tam = len(num)
#     print(f"Recebi os valores {num} e são ao todo {tam} números")
#
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# --------------------------------


# def dobra(lst):
#     pos = 0
#     while pos < len(lst): # dobrando o conteudo dentro de valores
#         lst[pos] *= 2
#         pos = pos + 1
#
#
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)


# --------------------------------

def soma(* valores):
    s = 0
    for num in valores:
        s = s + num
    print(f" Somando os valores {valores} temos {s}")


soma(5, 2)
soma(2, 9, 4)














