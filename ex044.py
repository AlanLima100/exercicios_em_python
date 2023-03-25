#ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
#- À VISTA DINHEIRO / CHEQUE: 10% DE DESCONTO
#- À VISTA NO CARTÃO: 5% E DESCONTO
#-EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# 3X OU MAIS NO CARTÃO: 20% DE JUROS
print("{:=^40}".format("\033[1;36;40m LOJAS ALANZINHO MAIS\033[m"))
valor = float(input("Qual o preço das compras?R$:"))
print("FORMAS DE PAGAMENTO")
print(""" 
[\033[32m1\033[m] à vista dinheiro/ cheque
[\033[33m2\033[m] à vista cartão
[\033[34m3\033[m] 2x no cartão
[\033[35m4\033[m] 3x ou mais no cartão""")
desconto10 = 10 * (valor / 100)
desconto5 = 5 * (valor / 100)
juros2x = valor / 2
juros20x = 20 * (valor / 100)
total20 = juros20x + valor
total5 = valor - desconto5
total10 = valor - desconto10
opcao = int(input("\033[1;0;40mQual é a opção escolhida?:"))
if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
    print("\033[1;31mOPÇÃO INVALIDA, TENTE NOVAMENTE!!\033[m")
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?:\033[m'))
    if parcelas <= 2:
        print("\033[31mNÚMERO DE PARCELAS INVALIDA!!\033[m \n\033[32mOPÇÃO 4 À PARTIR DE 3X OU MAIS, REFAÇA A COMPRA!!")
    else:
        print("O valor da compra foi de \033[32mR$ {}\033[m valores com parcelas de \033[32m{}x\033[m com acréscimo juros de \033[31m20%\033[m, novo valor a ser pago é de \033[32mR$ {}\033[m em \033[32m{}x\033[m de \033[32m{:.2f}\033[m".format(valor, parcelas, total20, parcelas,total20 / parcelas))
if opcao == 1:
    print("Sua compra será à vista no valor de \033[32mR$ {}\033[m você ganhou um desconto de \033[32m10%\033[m, novo valor a ser pago \033[32mR$ {}".format(valor, total10))
elif opcao == 2:
    print("Sua compra será à vista no valor de \033[31mR$ {}\033[m você ganhou um desconto de \033[32m5%\033[m, novo valor a ser pago \033[32mR$ {}".format(valor,total5))
elif opcao == 3:
    print("Valor da compra foi de \033[32mR$ {}\033[m em 2x de \033[32mR$ {}\033[m sem juros".format(valor, juros2x))







