#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.

import random
n1 = str(input("O primeiro aluno : "))
n2 = str(input("O segundo aluno : "))
n3 = str(input("O terceiro aluno : "))
n4 = str(input("O quarto aluno : "))

lista = [n1, n2, n3, n4]# indica lista
escolhido = random.choice(lista)
print(" O aluno escolhido para fazer a prova primeiro foi você: {:>10}".format(escolhido))


