#DESENVOLVA UM ALÓGICA QUE LEIA O PESO E ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
# ABAIXO DE 18.5: ABAIXO DO PESO - ENTRE 18.5 E 25: PESO IDEAL - 25 ATÉ 30: SOBREPESO - 30 ATÉ 40: OBESIDADE - ACIMA DE 40: OBESIDADE MÓRBIDA

peso = float(input("Qual é o seu peso?:"))
altura = float(input("Qual é sua altura?:"))

IMC = peso / (altura ** 2)
print("Seu IMC atual é de \033[32m{:.2f} Kg\033[m ".format(IMC), end="")

if IMC <= 18.5:
    print("Você está \033[31mabaixo\033[m do PESO procure uma NUTRICIONISTA!")
elif IMC <= 25:
    print("Você está com o peso \033[32mIDEAL!")
elif IMC <= 30:
    print("Você está com \033[31mSOBREPESO!")
elif IMC <= 40:
    print("Você está com \033[31mOBESIDADE!!")
else:
    print("Voce está com \033[31mOBESIDADE MÓRBIDA\033[m,\033[39m procure um MÉDICO E UM PROFISSIONAL DE EDUCAÇÃO FÍSICA")

#PROFESSOR
# peso =  float(input("Qual é o seu peso? (KG)"))
# altura = float(input("Qaul é sua altura? (m)"))
# imc = peso / (altura **2)
# print(("O IMC dessa pessoa é {:.1f}".format(imc)))
# if imc < 18.5:
#     print("Você está BAIXO  DO PESO normal")
# elif 25<= imc < 30:
#     print("PARABÉNS, você está na faixa de PESO NORMAL")
# elif 25 <= imc < 30:
#     print("Você está em SOBREPESO!")
# elif 30 <= imc < 40:
#     print("Você está em OBESIDADE!")
# else:
#     print("Você está em OBESIDADE MÓRBIDA, cuidado!!")