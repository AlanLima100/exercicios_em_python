#REFAÇA OS DESAFIO 009, MOSTRNADO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZNDO UM LADO FOR
m = int(input("Digite um número:"))
for c in range(1, 11):
    print(" {} x {} = {}".format(m, c, m*c))