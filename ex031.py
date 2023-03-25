#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200 KM e R$0.45 para viagens mais longas.

distancia = float(input("Qual é a distancia da sua viagem em KM? "))
kmc = distancia * 0.45

if distancia <= 200:

    km = distancia * 0.50


    print("O valor da passagem tem um custo  R$ 0.50 por cada km rodado ficando assim: {} ".format(km))


else:

    print(" A passagem tem um custo de R% 0.45 por KM acima de 200 km ficando assim {}".format(kmc))


#OUTRO JEITO COM O PROFESSOR:

distância = float(input("Qual é a distância da sua viagem?"))

print("Você está prestes a começar uma viagem de {} KM".format(distância))

if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print("E o preço da sua passagem será de R$ {:.2f}".format(preço))


# OUTRA MANDEIRA SIMPLIFICADA

distância = float(input("Qual é a distância da sua viagem?"))

print("Você está prestes a começar uma viagem de {} KM".format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print("E o preço da sua passagem será de R$ {:.2f}".format(preço))
