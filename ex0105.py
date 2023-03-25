
# FAÇA UM PROGRMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNO E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
# QUANTIDADE DE NOTAS
# A MAIOR NOTA
# A MENOR NOTA
# A MÉDIA DA TURMA
# A SITUAÇÃO (OPCIONAL)


def notas(*n, sit=False):
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(n)
    if sit:
        if r["media"] >= 7:
            r["situação"] = "BOA"
        if r["media"] >= 5:
            r["situação"] = "RAZOÁVEL"
        else:
            r["situação"] = "RUIM"
    return r


# Programa Principal
resp = notas(5,5, 2.5, 1.5, sit=True)
print(resp)
help(notas)