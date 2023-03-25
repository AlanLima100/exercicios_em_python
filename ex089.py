# CRIE UM PROGMRA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO Em UMA LISTA COMPOSTA. NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA
# QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE.
ficha = []
while True: # criei um lup até o usuário digitar "n" ou "N" na variável "parada"
    nome = str(input("Nome:")) # na variável nome pedi os nomes dos usuários
    nota1 = float(input("Nota 1°:"))# 1° nota do usuário
    nota2 = float(input("Nota 2°:"))# 2° nota do usuário
    media = (nota1 + nota2) / 2 # calculando a media entre a 1º e 2º nota
    ficha.append([nome, [nota1, nota2], media])# adicionando os nomes e notas tudo dentro da lista "ficha"
    parada = str(input("Quer continuar?: [S/N]")).strip().upper() # dentro de "parada"
    while parada not in "nNsS": # enquanto o usuário não digitar "nNsS" vai apareceer a seguinte mensagem...↓
        parada = str(input("Valor inválido! Quer continuar? [S/N]:")) # "S" pra "sim e "N" para "não"
    if parada == "N": # a resposta for "n" vai sair do LUP
        break
print("-=" * 30) # mostrando caracteres multiplicado 30x
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')# acrescentando caracteres para organizar a tela
print("-=" * 30)# mostrando caracteres multiplicado 30x
for i, a in enumerate(ficha): # falando no "i" o indice (posição de cada item) o "a" é o nome do aluno dentro de ficha.
    print(f"{i:<4} {a[0]:10}{a[2]:>8.1f}")# a[0] vai mostrar o nome de cada pessoa dentro de lista → o a[2] vai mostrar a media de cada usuário dentrod e lista
print(f'{len(ficha)}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
while True: #enquanto o "opc" não for "999" o lup não para
    print("_" * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(ficha):
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<< VOLTE SEMPRE >>>")
