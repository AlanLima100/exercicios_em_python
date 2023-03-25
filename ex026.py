#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A"  - Emq ue posição ela aparece a primera vez. - Em que posição ela aparece a última vez.

frase = str(input("Digite sua frase:")).strip()
cu = frase.upper()
print("A frase: {}  a letra => A <= aparece {} vezes já a sua primeira letra A começou na posição {} e a letra A aparece por ultimo na posição {}".format(cu, cu.count("A"), cu.find("A")+1, cu.rfind("A")+1))




