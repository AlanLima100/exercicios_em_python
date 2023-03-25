#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. ex: Ana Maria de Souza primeiro=Ana último: Souza

# nome = str(input("Digite seu nome completo:")).strip()
# print("Olá {}, prazer em te conhecer!".format(nome))
#
# lista = nome.split()
#
# print("O seu primeiro nome é: {} e o seu último nome é {}".format(lista[0], lista.pop()))

#OUTRA FORMA DE FAZER

nome = str(input("Digite seu nome completo:")).strip()

nome = nome.split()
print("Muito rpqazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é:{}".format(nome[len(nome)-1])) # Neste caso eu pedi que mostrassee nome vai pegar a lista do que foi diditado, depois com o len pedi para contar a lista vai mostrar o valor
# total da lista subsequente a última posição, como se inicia com  posição "0"(zero) o -1 e para eliminar essa posição.








