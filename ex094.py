#CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EMUMA LISTA. NO FINAL, MOSTRE:
# a) QUANTAS PESSOAS FORAM CADASTRADAS
# B) A MÉDIA DE IDADE DO GRUPO
# C) UMA LISTA COM TODSA AS MULHERES.
# D) UMA LISTA COM TODAS AS PESSOAS  COM IDADE ACIMA DA MÉDIA
dados = list()
nome = dict()
sexo = dict()
idade = dict()
soma = list()
mulheres = list()
cont = 0
while True:
    nome["nome"] = str(input("Digite seu nome:"))
    dados.append(nome.copy())
    cont = cont + 1
    sexo["sexo"] = str(input("Sexo → [M / F]:").strip().upper())
    dados.append(sexo.copy())
    if sexo["sexo"] in "F":
        mulheres.append(nome["nome"])
    while sexo["sexo"] not in "FM":
        sexo["sexo"] = str(input("VALOR INVÁLIDO!! Sexo → [M / F]:").strip().upper())
        if sexo["sexo"] in "FM":
            break
    idade["idade"] = int(input("idade?: "))
    soma.append(idade["idade"])
    dados.append(idade.copy())
    c = str(input("Quer continuar? [ S / N ]: ").strip().upper())
    while c not in "sSnN":
        c = str(input("Valor inválido !! Quer continuar? [ S / N ]: ").strip().upper())
    if c == "N":
        break
for k, v in enumerate(dados):
    print(f"{k} >>>>>>>> {v}")
total = sum(soma) / cont

print(f"Ao todo temos {cont} pessoas cadastradas ")
print(f" A média de idade dessas pessoas é de {total}")
print(f"As mulheres cadastradas foram {mulheres}")

# OUTRA FORMA DE FAZER

pessoa = list()
nome = dict()
soma = media = 0

while True:
    nome.clear()
    nome["nome"] = str(input("Digite seu nome:"))
    while True:
        nome["sexo"] = str(input("sexo? [F / M ]: ")).upper()[0]
        if nome["sexo"] in "FM":
            break
        print("Valor inválido, por favor digite 'F' ou 'M' ")
    nome["idade"] = int(input("idade?: "))
    soma = soma + nome["idade"]
    pessoa.append(nome.copy())
    while True:
        resp = str(input("Quer continuar?: [S / N]")).upper()[0]
        if resp in "SN":
            break
        print("Valor inválido! Por favor,  digite [ S / N]")
    if resp == "N":
        break
media = soma / len(pessoa)
print(f"Foram cadastras {len(pessoa)}")
print(f"A média de idade foi de {media:.2f} anos")
print("As Mulheres cadastradas foram:", end=" ")
for p in pessoa:
    if p["sexo"] in "Ff":
        print(f"{p['nome']},", end=" ")
print()
print("Listas das pessoas acim da média:")
for p in pessoa:
    if p["idade"] >= media:
        print("    ", end=" ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end=" ")
        print()
print("<<<<   FINALIZADO   >>>>>")






# PROFESSOR FEZ:
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F. ")
    pessoa["idade"] = int(input("Idade: "))
    soma = soma + pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer Continuar? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("ERRO!, Responda apenas S ou N. ")
    if resp == "N":
        break
print("-=-" * 30)
print(f"Ao todo temos {len(galera)} pessoas cadastradas. ")
media = soma / len(galera)
print(f" A Média de idade é de {media:5.2f} anos.")
print(f"As mulheres cadastradas foram", end="")
for p in galera:
    if p["sexo"] in "Ff":
        print(f"{p['nome']}", end="")
print()
print(f"Lista das pessoas que estão acima da média: ")
for p in galera:
    if p["idade"] >= media:
        print(" ", end="")
        for k, v in p.items():
            print(f"{k} = {v}", end="")
        print()
print("<< ENCERRADO >>")

