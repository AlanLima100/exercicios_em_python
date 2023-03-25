#FAÇA UM PRGRAMA QUE TENHA UMA FUNÇÃO CHAMA CONTADOR (), QUE RECEBA TRÊS PARÂMETROS: INICIO, FIM E PASSO  E REALIZE A CONTAGEM.
# SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
# A ) DE 1 ATÉ 10, DE 1 3M 1
# B ) DE 10 ATÉ 0, DE 2 3M 2
# V ) UMA CONTAGEM.
from time import sleep


def counter(i, f, p):
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    print("-=" * 25)
    print(f"Score in {i} até {f}  de {p} em {p}")
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.2)
            cont = cont + p
        print("fim")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.2)
            cont = cont - p
        print("fim")


counter(1, 10, 1)
counter(10, 0, 2)
print("-=" * 25)
print("Agora é sua vez de personalizar a contagem !")
ini = int(input("Start:  "))
end = int(input("The end: "))
step = int(input("Step:  "))
counter(ini, end, step)
