# FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTE0() E SOMARpAR(). a PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA E A SEGUNDA
# FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES pares SORTEADOS PELA FUNÇÃO ANTERIOR
from random import randint
from time import sleep


def sorteia():
    numeros = []
    print('Sorteando 5 valores da lista:', end= ' ')
    for i in range(0, 5):
        sleep(0.3)
        numeros.append(randint(1, 10))
        print(numeros[i], end=' ')
    print('PRONTO!')
    return numeros


def somPar(a):
    soma = 0
    print(f'Somando os valores pares de {a}, temos', end=' ')
    for k, v in enumerate(a):
        if v % 2 == 0:
            soma += v
    print(soma)

somPar(sorteia())

#professor fez:


from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n} ", end="", flush=True)
        sleep(0.3)
    print("Pronto!")


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f"Somando os valores pares dA LISTA: {lista}, temos {soma}")


sorteia(numeros)
somapar(numeros)

print(numeros)

