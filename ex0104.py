# CRIE UM PROGRAMA QUE TENHA A FUNÇÃO leiaInt(), que vai FUNCIONAR DE FORMA SEMELHANTE Á FUNÇÃO INPUT() DO PYTHON, Só QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS
# UM VALOR NUMÉRICO.

# EX: N = LEITAiNT("dIFGITE UM N")
def leiaInt(c):
    c = input(c)
    while True:
        if c.isdigit():
            return c
        else:
            c = input("\033[31mERRO! Digite um número: \033[m").strip()


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")

# eu fiz:

def leiaInt(n):
    while True:
        num = input(n)
        if num.isnumeric() is not True:
            print(f"\033[1;3;31mERRO! '{num}' Não é válido! Digite um número válido: \033[m", end="")
        else:
            return num


num = leiaInt("Digite um número: ")
print(f"Voce acabou de digitar o número {num}")


# internet:

def LeiaInt(num):
    while True:
        n = input(num)
        if n.isnumeric() is False:
            print('\033[1;3;31mERROR! Digite um numero inteiro válido.\033[m')
        else:
            return n


number = LeiaInt(f'{"=-"*20}=\ndigite um numero: ')
print(f'Você cabou de digitar o numero {number}.')


#professor:

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;3;31mERROR! Digite um numero inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt("Digite um número: ")
print(f"Voce acabou de digitar o número {n}")