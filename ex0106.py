# FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERACTIVE HELP DO PYTHON. O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECEER.
#QUANDO O USUÁRIO DIGITAR A PALAVRA "FIM", O PROGRAMA SE ENCERRARÁ. OB S: USE CORES.
from time import sleep

c = ("\033[m", # 0 - sem cor
     "\033[0;30;41m", # 1 - vermelho
     "\033[0;30;42m", # 2 - verde
     "\033[0;30;43m", # 3 - amarelo                  #VARIÁVEL "C" É GLOBAL
     "\033[0;30;44m", # 4 - azul
     "\033[0;30;45m", # 5 - roxo
     "\033[7;30m"     # 6 - branco
     );


def ajuda(com):
    titulo(f"Acessando o manual do comando \"{com}\"", 4)  # esse comando "\"{com}\" serve  A barra pode ser usada para se colocar aspas do mesmo tipo usado para abrir a string dentro da string.
    print(c[6], end="")
    help(com)
    print(c[0], end="")
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end="")
    sleep(1)


#comando principal
comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO !", 1)
