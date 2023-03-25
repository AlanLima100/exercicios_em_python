#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input("Qual é o preço deste produto?R:"))
desconto = 5 * (valor/100)
total = valor - desconto
print("Parabéns! você ganhou 5% de desconto, valor a pagarR$:{:.2f}".format(total))