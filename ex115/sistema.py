# CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITA CADASTRAR PESSOAS PELO NOME E IDADE EMUM ARQUIVO DE TEXTO SIMPLES.
# O SISTEMA SÓ VAI TER 2 OPÇÕES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS.

from ex115.lib.interface import *  #importando tudo da interface da 115
from ex115.lib.arquivo import *
from time import sleep

arq = "cursoemvideoo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastras", "Cadastrar nova Pessoa", "Excluir Pessoa", "Sair do Sistema"])
    if resposta == 1:
        lerArquivo(arq)  # OPÇÃO DE LISTAR O CONTEUDO DE UM ARQUIVO
    elif resposta == 2:
        # OPção de cadastrar uma nova pessoa.
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho("EXCLUIR PESSOAS\n")
        lerArquivo(arq)

    elif resposta == 4:
        cabeçalho("Saindo do Sistema ... Até logo!")
        break
    else:
        print("\033[1;31mERRO! Digite uma opção válida\033[m")
    sleep(1)

print(dir(arq))
