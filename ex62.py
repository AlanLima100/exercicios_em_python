#MEHLORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TREMOS. O PROGRAMA ECERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 (ZERO) TERMOS.
num = int(input("Digite o primeiro termo:"))
razão = int(input("Digite a razão:"))
cont = 0
s = 0
total = 10
while cont < 10:
    print(" {} → ".format(num),end="") # "r" tá recebendo o primeiro termo que chamei de "num", logo r = 2 + 5, so fiz substituir r = 5 e razão = 5 se eu pôr, então o contator vai contar até
    num = num + razão                   # for igual a 10 e parar.
    cont = cont + 1
    if cont == 10:
        s = int(input("Quantos termos quer usar a mais?:"))
        cont = cont - s
        total = total + s

print(" Ao todos são {} termos".format(total))




#PROFESSOR FEZ ASSIM:

primeiro = int(input("Digite o primeiro termo:"))
r = int(input("Digite sua razão da PA:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} → ".format(termo), end="")
        termo = termo + r
        cont = cont + 1
    print("Pausa")
    mais = int(input("Quantos termos quer usar a mais?:"))
print(("progressão finalizada com {} termos".format(total)))





