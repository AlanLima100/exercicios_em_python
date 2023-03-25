#CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES. SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESES ABERTOS E FECHADOS NA ORDEM
# CORRETA.



#PROFESSOR FEZ:

expr = str(input("Digite a expressão:"))
pilha = []
for sim in  expr:
    if sim == "(":
        pilha.append("(")
    elif sim == ")":
        if len(pilha) > 0:
            pilha.pop() # remove o último elemento
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")

