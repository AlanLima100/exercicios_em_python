#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMA FICHA((), QUE RECEBA DOIS PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU.
# O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE.

def ficha(nome="", gols=""):
    if nome == "":
        nome = "DESCONHECIDO"
    if not gols.isdigit():
        gols = 0
    print(f"O jogador {nome} fez {gols} gols no campeonato")


nome = input("Nome do jogador?:").strip().title()
gols = input("Números de gols?:").strip()
ficha(nome, gols)




# COMO PROFESSOR FEZ:
def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato")


nome = str(input("Nome do jogador?:").title())
gols = str(input("Números de gols?:"))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == "":
    ficha(gols=gols)
else:
    ficha(nome, gols)

