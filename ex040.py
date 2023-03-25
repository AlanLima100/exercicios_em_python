#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRNADO UMA MESANGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:

nota = float(input("Qual o valor da sua primeira nota?:"))
nota1 = float(input("Qual o valor da sua segunda nota?:"))

media = (nota + nota1) / 2


print("Sua média foi {}".format(media))
if media <= 5.0:
    print(" \033[31mVocê foi REPROVADO!")
elif media >= 7.0:
    print("\033[32mVoce foi APROVADO!!")
elif media >= 5.1 or media <= 6.9:
    print("\033[36mVocê está de RECUPERAÇÃO!!")


