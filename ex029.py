#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
#SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA km ACIMA DO LIMITE.

velocidade = float(input("Qual velocidade que você passou? KM/H:"))

multa = (velocidade - 80) * 7.00

print("A velocidade que você passou foi de: {:.2f} KM/H".format(velocidade))
if velocidade >80:
    print("Você ultrapassou o limite permito nesta rodovia que era de 80 KM/H, voCê foi multado com o valor de R$ {:.2f}!".format(multa))
else:
    print("Você está dentro da velocidade permitida, PARABÉNS!!")

####OUTRA MANEIRA DE FAZER UTILIZANDO APENAS UM "IF" CONDIÇÃO SIMPLES É CHAMADO.
velocidade = float(input("Qual é a velocidade atual do carro?"))
if velocidade >80:
    print("MULTADO! você excedeu o limite permitido que é de 80km/h")
    multa = (velocidade-80) * 7
    print("Você deve pagar uma multa de R${:.2f}!".format(multa))
print("Tenha um bom dia! Dirija com segurança!")