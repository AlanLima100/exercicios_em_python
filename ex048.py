#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚEMROS IMPARES QUE SÃO MÚLTIMOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500
soma = 0
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:   #ou soma += impar
        cont = cont + 1  #ou  cont +=1
        soma = soma + impar
print("\nA soma de todos os {} valores solicitados é {}".format(cont, soma))
