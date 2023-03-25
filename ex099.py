# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMA MAIOR(), QUE RECEBA VÁRIOS PARÃMETROS COM VALORES INTEIROS. sEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR.
# PARAMENTROS
# VARIAVEIS
# DESEMPACOTAMENTO DE PARAMETROS
from time import sleep



def maior(* num): # varios numeros e desempacotar, vou receber varios parametros utiliza-se "*" na frente do parametros e quero desempacotar eles utilizando o "for"
    cont = superior = 0
    print("\nAnalisando os valores passados...")
    for valor in num:
        print(f" {valor} ", end="", flush=True)
        sleep(0.3)
        if cont == 0:
            superior = valor
        else:
            if valor > superior:
                superior = valor
        cont = cont + 1
    print(f"Foram informados {cont} valores ao todo. ")
    print(f"O maior valor informado foi {superior}. ")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0, )
maior(1, 2)
maior(6)
maior()
