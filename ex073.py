#CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
# A) APENAS OS 5 PRIMEIROS COLOCADOS.
# B) OS ÚLTIMOS 4 COLOCADOS DA TABELA.
# C) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA.
# D) EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE.


times = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará SC", "Internacional", "São Paulo",
"Atthletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport Recife", "Chapecoense")
print("=-" * 50)
print("Os 5 primeiros colocados do brasileirão 2021 são:", end="")
print(times[0:5])
print("=-" * 50)
print("Os 4 últimos colocados do Brasileirão 2021 são:", end="")
print(times[-4:])
print("=-" * 50)
print("Times em ordem Alfabética:", end="")
print(sorted(times))
print("=-" * 50)
print(f"O Chapecoense está {times.index('Chapecoense')+1}º posição da Tabela do Brasileirão 2021")
