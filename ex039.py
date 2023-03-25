#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE: - SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR. - SE É A HORA DE SE ALISTAR. - SE JÁ PASSOU
# DO TEMPO DO ALISTAMENTO.  SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPOM QUE FALTA OU QUE PASSOU DO PRAZO.
from datetime import date
ano = int(input("Qual é o ano do seu  nascimento?:"))

anoatual = date.today().year - ano
if anoatual == 17 or anoatual == 18:

    print("você tem {} anos já é hora de se alistar no exercito".format(anoatual))

elif anoatual < 17:
    print("Você só tem apenas {} anos, você ainda vai se alistar no exercito no tempo certo.".format(anoatual))
    b = 17 - anoatual
    b1 = b + date.today().year
    print("Ainda falta(am) {} anos(os), seu alistamento deverá ocorrer em {}".format(b, b1))
else:
    print("Sua idade é de {} anos em {} já possou do tempo de alistamento militar".format(anoatual, date.today().year))
    c = anoatual - 18
    c1 = date.today().year - c
    print("Voce já está atrasado {} ano(os), seu alistamento deveria ter ocorrido em {}".format(c, c1))







