# #Aula 010
#
# nome = str(input("Qual é seu nome?"))
# if nome == "Alan Vitor":
#     print("Que nome lindo você tem!")
# else:
#     print("Seu nome é tão normal!")
# print("Bom dia, {}!".format(nome))

#FAÇA A MEDIA ENTRE DUAS NOTAS
n = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))

m = (n + n2) / 2

print("A sua média foi: {:.1f}".format(m))
if m >=6.9:
    print("Sua nota está acima média, PARABÉNS!!")
else:
    print("Sua nota foi abaixo do esperado, você foi reprovado, ESTUDE MAIS!!!")

