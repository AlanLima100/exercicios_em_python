# bliblioteca da interface do ex115

def leiaInt(msg):
    while True:
        try: # tente fazer isso aqui...
            n = int(input(msg)) # mostrar o que ja foi feito até o momento...
        except (ValueError, TabError): # se for  erro de valor ou erro de tipo... mostre isso..
            print("\033[31mERRO: por favor, digite um número inteiro válido. \033[m")
            continue  # joga direto pro While de novo tentar mais uma vez, se não der problema e tudo der certo return "n"
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esses número. \033[m")
            return 0
        else:
            return n


def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c} \033[m- \033[34m{item}\033[m")
        c = c + 1
    print(linha())
    opc = leiaInt("\033[1;32mSua Opção: \033[m") # estou substituindo "int, input" pelo "opc = leiaInt"
    return opc



