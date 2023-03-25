from ex115.lib.interface import *
import csv


def arquivoExiste(nome): # nome do arquivo
    try:# tente fazer o seguinte...tratamento de erro, pra verificar se um arquivo existe.
        a = open(nome, "rt")  #a função "open" tenta abrir um aquivo em modo texto, rt significa leitura e text modo texto
        a.close() #fechar  o arquivo
    except FileNotFoundError:  #exceção se o arquivo não for encontraro "FileExistsError" ← tratamento de erro
        return False # AQUIVO NÃO ENCONTRADO
    else: # ou seja, seu eu achei o aquivo ele abriu e fechou...
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+") # escrever um aquivo de texto, se a caso ele não exista "+" ele cria um
        a.close() # pra fechar
    except:
        print("houve um ERRO na criação do aquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    cont = 0
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler arquivo")
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        # print(a.read()) # pega as linhas do meu arquivo e joga dentro de uma lista
        for linha in a:
            cont = cont + 1
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{cont} - {dado[0]:<30}{dado[1]:>3} anos ")


def cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado. ")
            a.close()







