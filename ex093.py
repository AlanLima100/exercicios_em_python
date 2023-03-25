# CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI TER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM
# CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO.
# dados = dict()
# gols = list()
# partidas = list()
# cont = 0
# dados["nome"] = str(input("Name?:"))
# partidas.append(int(input(f"Quantas partidas {dados['nome']} jogou?: ")))
# for r in range(1, partidas[0] + 1):
#     gols.append(int(input(f"Quantos GOLS na {r}ª partida?: ")))
# print("-=-" * 30)
# print(f"{dados} fez :{gols} gols por jogo em um total de {partidas} partidas, ao todo foram {sum(gols)} gol")
# print("-=-" * 30)
# for k, v in enumerate(partidas):
#     print(f"O jogador {dados['nome']} jogou {v} partida(as).")
# for v in gols:
#     for k, ve in enumerate(partidas):
#         cont = cont + 1
#         print(f"   ==>> Na partida {cont}° fez {v} Gols.")
# print(f"Foi um total de {sum(gols)} gols")


#COMO O PROFESSOR FEZ:
jogador = dict()
partidas = list()
jogador["nome"] = str(input("Nome do jogador: "))
tot = int(input(f"Quantas partidas {jogador['nome']} jogou?"))
for c in range(0, tot):
    partidas.append(int(input(f"   Quntos gols na partida {c +1}°?")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
print("-=-" * 30)
print(jogador)
print("-=-" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("=-" * 30)
print(f" O Jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i, v in enumerate(jogador['gols']):
    print(f"    => Na partida {i+1}°, fez {v} gols. ")
print(f"Foi um total de {jogador['total']} gols. ")