# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO QUALQUER COMO PARâmetro e mostre uma mensagem com tamanho adaptável.
# ex: escreva("Olá, mundo!")
def escreva(nome):
    tam = len(nome)
    print("~" * len(nome))
    print(nome)
    print("~" * len(nome))


escreva("Alan Vitor Cândido")
escreva("Cachorro")
escreva("Curso de Python no YouTube")
