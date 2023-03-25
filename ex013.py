#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Qual é o seu salário?:"))
aumento = 15 * (salario/100)
novo_salario = salario + aumento
print("O seu novo salário com 15% de aumento é {}".format(novo_salario))
