# APRIMORE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR.
jogador = dict()
partidas = list()
resultado = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou?"))
    for c in range(0, tot):
        partidas.append(int(input(f"   Quantos gols na partida {c +1}°?")))
        jogador["gols"] = partidas[:]
        jogador["total"] = sum(partidas)
    resultado.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S / N]")).upper().strip()[0]
        if resp in "SN":
            break
        print("Resposta inválida,'S' para SIM ou 'N' para NÃO ")
    print("=-" * 30)
    if resp in "Nn":
        break
print("=-=" * 35)
print(f"{'COD NOME':<15}{'GOLS':>15}{'TOTAL':>20}")
print("_____" * 20)
for k, v in enumerate(resultado):
    print(f"{k+1}°{v['nome']:.<22}{v['gols']}{v['total']:.^15}")
while True:
    print("-=" * 30)
    opc = int(input("MOSTRAR DADOS DE QUAL JOGADOR? [ Digite  N° do Jogador ] ( 999 para parar ): "))
    opc = opc - 1
    if opc == 998:
        print("<<<<VOLTE SEMPRE >>>...")
        break
    if opc >= len(resultado):
        print(f"ERRO! Não existe jogador com este valor!")
    else:
        print(f" ---LEVANTAMENTO DO JOGADOR {resultado[opc]['nome']}")
        for k, v in enumerate(resultado[opc]['gols']):
            print(f"   No {k+1}° jogo fez {v} gols ")
        print(f"Foi um total de {jogador['total']} gols. ")
        print("=-=" * 35)
print("<<< VOLTE SEMPRE >>>")

#COMO O PROFESSOR FEZ:
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    tot = int(input(f" Quanas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f" quantos gols na partida {c+1}?")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/ N]")).upper()[0]
        if resp in "SN":
            break
        print("Erro! Responda apenas S ou N. ")
    if resp == "N":
        break
print("-" * 30)
print("COD ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f" {k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Nãao existe jogador com código {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"   No jogo {i + 1} fez {g} gols ")
    print("=" * 40)
print("<< VOLTE SEMPRE>>")





