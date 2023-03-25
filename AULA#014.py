
n = 1  #começa com "1"
par = impar = 0 #desse jeito o programa identifica o "0" como um número par.
while n != 0:	#enquanto o número for diferente de zero/ enquanto não for digitado o "0"
	n = int(input("Digite um valor: "))
	if n != 0: # resolvendo a questão do "0" ser par.
		if n % 2 == 0:
			par = par + 1
		else:
			impar = impar + 1
print("Você digitou {} números pares e {} número ímpares!".format(par, impar))