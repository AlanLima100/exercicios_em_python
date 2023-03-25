# 109 - MODIFIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO 107 PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE O LVAOR RETORNADO POR ELAS VAI SER OU NÃO FORMATADO
#PELA FUNÇÃO moeda(), desenvolvida no desafio 108.
def metade(n=0, formato=False):
    """

    :param n: Valor do parametro
    :param formato: Se falso não não recebe o paramento se True (verdade) recebe a função "moeda"
    :return: "res" está recebendo "p"valor do usuário.
    """
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n=0, formato=False): # aumenta 10% do valor
    res = n + (n / 10)
    return res if formato is False else moeda(res)


def diminuir(n=0, formato=False): # diminuir 13% fo valor
    res = n - (n / 13)
    return res if formato is False else moeda(res)


def moeda(n=0):
    return f"{n:>.2f}".replace(".", ",")
