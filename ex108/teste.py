# 108 - ADPTE O CÓDIGO DO DESAFIO 107, CRIANDO UMA FUNÇÃO ADICONAL CHAMADA MOEDA() QUE CONSIGA MOSTRAR OS VALORES COMO UM VALOR MONETÁRIO FORMATADO.
from ex108 import moeda

p = float(input("Digite o preço: R$ "))
print(f" A ......metade de R${moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de R${moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f" Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p))}")
print(f"Reduzindo.... 13%, temos R${moeda.moeda(moeda.diminuir(p))}")
