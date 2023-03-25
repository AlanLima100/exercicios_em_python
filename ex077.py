#CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS ( NÃO USAR ACENTOS). DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS.
palavras = ("Aprender", "Programar", "Linguagem", "Python", "Curso", "Gratis",
            "Estudar", "Praticar", "Trabalhar", "Mercado", "Programador", "Futuro")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for letra in p: #para cada letra na palavra "p"
        if letra.lower() in "aeiou":
            print(letra, end=" ")

lanche = ("hambúrguer", "suco", "pizza", "pudim", "batata Frita")
for cont in range(0, len(lanche)):
    print(lanche[cont])

