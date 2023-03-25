#   CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR. NO FINAL, MOSTRE:
# A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
# B) QUANTOS HOMENS FORAM CADASTRADOS.
# C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.

cont = 0
pessoasmaisde18 = 0
homens = 0
mulheresmenosde18 = 0
while True:
    frase = str("CADASTRE UMA PESSOA")
    print("-=" * 20)
    print(f"{frase.center(40)}")
    idade = int(input("Qual é sua idade?:"))
    sexo = str(input("Qual é o seu sexo?[M/F]:").upper().strip())
    while sexo not in "M" and sexo not in "F":
        sexo = str(input("Valor invalido! Qual seu sexo ? [M/F]:").strip().upper())
    cont = cont + 1
    if idade >= 18:
        pessoasmaisde18 = pessoasmaisde18 + 1
    if sexo == "M":
        homens = homens + 1
    if sexo == "F" and idade < 20:
        mulheresmenosde18 = mulheresmenosde18 + 1
    c = str(input("Quer continuar? [S/N]:").upper().strip())
    while c not in "S" and c not in "N":
        c = str(input("Valor invalido! Quer continuar? [S/N]:").strip().upper())
    if c == "N":
        break
print("="*20)
print("FIM DO PROGRAMA")
print("="*20)
print(f"O total de {pessoasmaisde18} pessoas com mais de 18 anos.")
print(f"Ao todo temos {homens} homens cadastrados.")
print(f"E temos um total de {mulheresmenosde18} mulheres com menos de 20 anos")
print(f"Ao todo foram {cont} de pessoas que participaram")

#COMO O PROFESSOR FEZ:

tot18 = totH = totM20 = 0
while True:
    idade = int(input("Idade:"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totH += 1
    if sexo == "F" and idade < 20:
        totM20 += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar ? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {tot18}")
print(f"Ao todo temos {totH} homens cadastrados")
print(f"E temos {totM20} mulheres com menos de 20 anos")