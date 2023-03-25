# 108 - ADPTE O CÓDIGO DO DESAFIO 107, CRIANDO UMA FUNÇÃO ADICONAL CHAMADA MOEDA() QUE CONSIGA MOSTRAR OS VALORES COMO UM VALOR MONETÁRIO FORMATADO.

def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0): # aumenta 10% do valor
    n = n + (n / 10)
    return n


def diminuir(n): # diminuir 13% fo valor
    n = n - (n / 13)
    return n


def moeda(n=0):
    return f"{n:>.2f}".replace(".", ",")
