# - 107 - CRIE UM MÓDULO CHAMADO moeda.py que tenha AS FUNÇÕES INCORPORADAS aumentar(), diminuir(), dobro() e metade(). faça também um programa que importe esses módulo e use
# Algumas dessas funções.

import moeda

p = float(input("Digite o preço: R$ "))
print(f" A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f" Aumentando 10%, temos {moeda.aumentar(p)}")
print(f"Reduzindo 13%, temos {round(moeda.diminuir(p), 2)}")
