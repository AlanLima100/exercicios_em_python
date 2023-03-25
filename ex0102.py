# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E O OUTRO CHAMADO SHOW, QUE SERÁ UM VALOR
# LÓGICO (OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CÁLCULO DO FATORIAL.
def fatorial(n, show=False):
    """
    → Calculad o Fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show: # se show for verdade
            print(c, end="")
            if c > 1:
                print(f" x ", end="")
            else:
                print(" = ", end="")
        f = f * c
    return f


n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}")

print(fatorial(n, show=True))
