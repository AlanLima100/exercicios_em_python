#FAÇA UM PROGMRA QUE LEIA UM ANO QUALQUER E MOSTE SE ELE É BISSEXTO.

# ano = int(input("Digite o ano para saber se ele é BISSEXTO: "))
#
#
# if (ano % 4) ==0:
#     print(" O ano de {} é um ano BISSEXTO".format(ano))
# else:
#     print(" O ano {} , NÃO é um ano BISSEXTO".format(ano)) #obs: Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os anos normais de 365 dias.
#     #ocorrendo a cada quatro anos ( exceto anos múltiplos de 100 que não são múltiplos de 400).

# Professor corrigiu esse problema:
from datetime import date
ano = int(input("Que ano quer analisar? Coloque o 0 para analisar o ano atual:"))
if ano == 0:
    ano = date.today().year # pegar o ano atual, pegar a data de hoje configurada na máquina, vai pegar só o ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # ele tem que ser divisivel por 4 e tbm não pode ser divisivel por 100 (and ano % 100) não pode ser diferente de zero (!=0) ou então (or) o ano % 400 ==0:
    print("O ano {} é BISSETO".format(ano))
else:
    print("O ano {} NÂO é BISSEXTO".format(ano))