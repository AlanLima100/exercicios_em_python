# seu eu pegar o comendo :
# se eu quiser 10x
#
# for c in range(1, 6): # vi mostrar 5 vezes, porq de um até seis, pq ele vai fazer de um até cinco e no seix ele para
# 	print("oi")   # não considera o ultimo número.
# print("FIM')
#
# -------------
# for c in range(1, 6): # vai aparecer "oi" e "fim" alternados pois o último "print" tá dentro do for
# 	print("oi")
# 	print("FIM')
#
# --------------
# for c in range(1, 6): #  se no lugar de "oi" escrever "print(c)"
# 	print("c")
# print("FIM')
#
# vai mostrar#:
# 0
# 1
# 2
# 3
# 4
# 5
# FIM # LEMBRAR que ele ignora o último número.
# ----------------------------------
# se eu quiser uma contagem de 6 até 0 (seis até zero)
#
# for c in range(6, 0):
# 	print("c")
# print("FIM')
#
# vai mostrar#:
# FIM
#
# SE EU quiser contar regressivamente:
#
# for c in range(6, 0, -1): # é como se ele entrasse no laço e eliminasse -1, voltasse e eliminou -1 outra vez
# 	print("c")
# print("FIM')
#
# vai mostrar#:
# 6
# 5
# 4
# 3
# 2
# 1
# FIM
#
# --------------
# contando de zero a sete pulando de dois em dois
#
#
# for c in range(0, 7, 2): #
# 	print("c")
# print("FIM')
#
# vai mostrar#:
# 0
# 2
# 4
# 6
# FIM
# ---------------------
# n = int(inout("Digite um número:"))
# for c in range(0, n):
# 	print(c)
# print("FIM")
#
# vai mostrar#: vai mostrar do zero (0) até o número colocado em 'n' -1
# ex: colocando 7 em "n"
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# FIM
# ------------------------------------
# SE EU QUISSE QUE FOSSE ATÉ O NÚMERO 7 MEMSO ERA SÓ SOMAR +1
# n = int(inout("Digite um número:"))
# for c in range(0, n+1):
# 	print(c)
# print("FIM")
#
# vai mostrar#: vai mostrar do zero (0) até o número colocado em 'n' +1
# ex: colocando 7 em "n"
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# FIM
# --------------------------
# NESTE EXEMPLo estou pedindo para o que for escrito em "início"(i) vá até o que for escrito em "fim"(f) pulando de o que for escrito em "Passo"(p)
#
# i = int(input("Início:"))
# f = int(input("Fim: "))
# p = int(input(Passo:"))
# for c in range(i, f+1, p):
# 	print(c)
# print("FIM")
#
#
# vai mostrar#:inicio: 1 fim:5 passo: 1
# 1
# 2
# 3
# 4
# 5    #OBS: iria mostrar até 4 mais como eu somei +1 no comando (f+1)
# FIM
# ----------------------------
#
# for c in range (0,3):
# 	n = int(input("Digite um valor:"))
# print("fim")
#
# #Você só ler uma vez só que o comando "n" tá dentro do "for", entãos e o for vai contecer tres vezes então ele vai ler o número três vezes
#
#
# vai mostrar#
# Digite um valor:2
# Digite um valor:8
# Digite um valor:5
# FIM
#
# ------------------------------------
# AGORA SE EU QUERO UM SOMATORIO
#
# s = 0
# for c in range(0,4):
# 	n = int(input("Digite um valor:"))
# 	s = s + n #que no python tbm pode ser escrito "s+=n" mesma coisa
# print("O somatório de todos os valores foi {}".format(s))
#
#
#
# vai mostrar#
# Digite um valor:4
# Digite um valor:2
# Digite um valor:3
# Digite um valor:1
#
# O somatório de todos os valores foi 10
