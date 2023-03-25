#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O  USUÁRIO ESCOLHA QUAL SERÁ A BASE DE CONVERSÃO: 1- PARA BINÁRIO 2- PARA OCTAL 3- PARA HEXADECIMAL

num = int(input('digite um número:'))
print('''Escolha uma opção para conversão:
[1] conversor para BINÁRIO
[2] conversor para OCTAL    
[3] conversor para HEXADECIMAL''')
opção = int(input("Sua opção:"))
if opção == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif opção == 2:
    print(" {} convertieo para OCTAL é igual a {} ".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("opção invalida. Tente novamente.")
