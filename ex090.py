# FAÇA UM PROGRMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIOÁNIO. NO FINAL MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA.


aluno = dict()
todos = list()
situacao = list()

aluno["nome"] = str(input("what is your name?:"))
aluno["media"] = float(input("What is your media?:"))
print(aluno)
if aluno["media"] >= 7:
    print("Parabéns, Sua situação: APROVADO!!")
elif aluno["media"] >= 5 and aluno["media"] < 7:
    print("Você está em RECUPERAÇÃO!!")
else:
    print("Situação: REPROVADO!!")

for i in aluno.items():
    print(f" {i} ")


# PROFESSOR FEZ:

aluno = dict() # criando um dicionãrio
aluno["nome"] = str(input("Nome: ")) # este conteúdo vai para dentro de aluno dicionário
aluno["media"] = float(input(f" Media de {aluno['nome']}:")) # pedindo para pôr a media "nome" puxei o nome
if aluno["media"] >= 7: # Se o valor da media de aluno for maior ou igual a 7...
    aluno["situação"] = "Aprovado" # adicione no final da  biblioteca aluno se a media for mais igual a 7
elif 5 <= aluno["media"] < 7: # se for  media de aluno for menor que 7 e maior que 5...
    aluno["situação"] = "Recuperação" # adicione no final da  biblioteca aluno  situação = Recuperação
else:
    aluno["situação"] = "Reprovado"# se for difrente de tudo que está a cima mostre  situação = "Reprovado"
print("-=" * 30)
for k, v in aluno.items(): # para cada item em dentro de aluno...
    print( f"  - {k} é igual a {v}") # "k" será o 1° item (nome) e "v" 2° item (Alan) isso vai acontecer até o fim da lista de aluno.items()
                                    #  depois media é igual a o valor da media que foi informado pelo usuário
                                    # por fim vai motrar a situação dele, aprovado, recuperação ou reprovado.

print(aluno)
