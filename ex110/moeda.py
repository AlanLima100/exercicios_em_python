# 110 - ADICIONE AO MÓDULO moeda.py criando nos desafios anteriores, uma função chama resumo(), que mostre na tela algumas informações geradas pelas funções que já temos
#MÓDULO CRIADO ATÉ AQUI
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
    res = n + (n * 10) / 100
    return res if formato is False else moeda(res)


def diminuir(n=0, formato=False): # diminuir 13% fo valor
    res = n - (n * 5) / 100
    return res if formato is False else moeda(res)


def moeda(n=0):
    return f"{n:>.2f}".replace(".", ",")


def resumo(n=0):
    print("-=" * 25)
    print("RESUMO DO VALOR".center(30))
    print("-=" * 25)
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço: \t{dobro(n, True)}")
    print(f"Metade do preço: \t{metade(n, True)}")
    print(f"10% de aumento: \t{aumentar(n, True)}")
    print(f"5% de redução: \t\t{diminuir(n, True)}")
    print("-=" * 25)
