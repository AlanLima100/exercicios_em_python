#ESCREVA UM PROGMRA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM: - O PRIMEIRO VALOR É MAIOR - O SEGUNDO VALOR É MAIOR - NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.

num = int(input("Digite um número:"))
num1 = int(input("idigte outro número:"))

if num > num1:
    print("\033[34mO primeiro número {} é maior que o segundo {}".format(num, num1))
elif num < num1:
    print("\033[33mO segundo número  {} é maior que o primeiro número {}".format(num1, num))
else:
    print("\033[32mNão existe valor maior, os dois são iguais")
