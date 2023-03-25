#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES "M" OU "F". CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.


Feminino = "F"
Masculino = "M"
sexo = str(input("Qual é o seu sexo? [M/F]")).upper().strip()[0]  # tirando os espaços, jogando para maiusculo e pegando a primeira letra
while sexo not in "MmFf": # ENQUANTO SEXO NÃO FOR IGUAL A "MmFf" me mostre isso:
    sexo = str(input("Valor invalido, tente outra vez! Qual o seu sexo?:")).strip().upper()[0]

if sexo == "F":
    print("Sexo FEMININO registrado com sucesso")
elif sexo == "M":
    print("Sexo MASCULINO registrado com sucesso")

# como eu fiz
sexo = str(input("Qual é o seu sexo [S/M]?:")).strip().upper()
while sexo not in "F" and sexo not in "M":
    sexo = str(input("Valor invaliado, tente outra vez, qual seu sexo?:")).strip().upper()
print("O sexo {} foi registrado".format(sexo))











