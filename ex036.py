# Escreva um programa para aprovar o empréstimo bancário para a compra deuma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCERDER 30% DO SALÁRIO OU ENTÃO O EMPRÈSTIMO SERÁ NEGADO.

print ("\033[32mOlá, sabemos que você deseja um financiamento para compra do seu imóvel, nosso Banco \033[35mAlanBank\033[m \033[32mpode te ajudar, mas antes precisamos que nos informe alguns dados...\033[m")
valordacasa = float(input("Qual é o valor o imóvel desejado? \033[32mR$: \033[m"))
salario = float(input("Qual é o valor da sua renda mensal? \033[32mR$: \033[m"))
anosapagar = int(input("Em quantos anos o Sr° predente pagar o financiamento?:"))

tempo = anosapagar * 12
parcela = valordacasa / tempo
if parcela > 30 * (salario / 100):
    print("\n\033[31mInfelizmente você não pode financiar este imóvel!!, o valor dá parcela ficou \033[32mR${:.2f}\033[m excedendo 30% do seu salário\033[m, \033[30;41mO EMPRÉSTIMO FOI NEGADO!!\033[m".format(parcela))
else:
    print("\nVoce optou em pagar pelo tempo de {} ano(os), logo serão {} meses, o valor das parcelas em {} ano(os) será de \033[32mR${:.2f}\033[m".format(anosapagar, tempo, anosapagar, parcela))
    print("\033[32mPARABENS!!!\033[m Seu empréstimo foi \033[30;42mAPROVADO!!!\033[m")

#PROFESSOR FEZ:
# casa = float(input("Valor da acsa: R$"))
# salário = float(input("Salário do comprador: R$"))
# anos = int(input("Quantos anos de financiamento?"))
# prestação = casa / (anos * 12)
# mínimo = salário * 30 / 100
# print(" Para pagar uma casa de R${:.2f} em {} anos".format(casa, anos), end="")
# print("a prestação será de R$ {:.2f}".format(prestação))
# if prestação <= mínimo:
#     print("Empréstimo pode ser CONCEDIDO!")
# else:
#     print("Empréstimo NEGADO!!")


