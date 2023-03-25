#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DE SEU AUMENTO.

#PARA SALÁRIO SUPERIORES A R$1.250,00, CALCULE UM AUMENTO DE 10%
#PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.


salario = float(input("Digite o valor do seu salário:"))
aumento = 10 * (salario / 100)
aumento2 = 15 * (salario / 100)
if salario > 1250.00:
    print("você recebeu um aumento de\033[32m 10%\033[m, seu novo salário é: \033[32mR${} PARABÉNS!!".format(aumento + salario))
else:
    print("Você recebeu um aumento de \033[32m15%\033[m, seu nonovo salário é: \033[32mR${} , PARABÉNS!!".format(aumento2 + salario))


#JEITO QUE O PROFESSOR FEZ:

# salário = float(input("Qual é o salário do funcionário?R$"))
# if salário <= 1250:
#     novo = salário + (salário * 15 / 100)
# else:
#     novo = salário + (salário * 10 / 100)
# print("Quem ganhava \033[4;32mR$ {:.2f} \033[m passa a ganhar \033[4;31mR$ {:.2f}\033[m agora.".format(salário, novo))