def leadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[31;21mErro: '{entrada}' é um preço inválido! \033[m")
        else:
            valido = True
            return float(entrada)


def leiaInt(c): # ler valores inteiro.
    c = input(c)
    while True:
        if c.isdigit():
            return c
        else:
            c = input("\033[31mERRO! Digite um número inteiro valido: \033[m").strip()


