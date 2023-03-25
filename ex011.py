#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
#para pintá-la, sabendo que cda litro de tinta pinta uma área de 2m².

a = float(input("Qual é altura da área?:"))
l = float(input("Qual é a largura área?:"))
m2 = a * l
t = m2 / 2
print("Sua área possui: {}m²".format(m2))
print("Logo, {:.2f} litros de tinta é o suficiente para pintar {:.2f}m²".format(t,m2))