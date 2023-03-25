# 109 - MODIFIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO 107 PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE O LVAOR RETORNADO POR ELAS VAI SER OU NÃO FORMATADO
#PELA FUNÇÃO moeda(), desenvolvida no desafio 108.
from ex109 import moeda

p = float(input("Digite o preço: R$ "))
print(f" A ......metade de R${moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"O dobro de R${moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f" Aumentando 10%, temos R${moeda.aumentar(p, True)}")
print(f"Reduzindo.... 13%, temos R${moeda.diminuir(p, True)}")
