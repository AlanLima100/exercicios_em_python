# frase = "Curso em Vídeo Pyhton"
# print(frase[3:13]) # dá posição 3° até a 13°

# frase = "Curso em vídeo Python"
# print(frase[:13]) #Do inicio não até a casa 13°

# frase = "Curso em Vídeo Pyhton"
# print(frase[13:]) # Da casa 13° até o fim

# frase = "Curso em Vídeo Python"
# print(frase[1:15:2])# Da casa 1° até a 15° pulando de 2 em 2 casas

# frase = "Curso em Vídeo Python"
# print(frase[1::2]) # Não disse até onde vai, mas disse que vai da casa 1° pulando de 2 em 2

# frase = "Curso em Vídeo Python"
# print(frase[::2]) # Não disse o inicio nem o fim, mas disse que vai  pulando de 2 em 2 casas

# frase = "Curso em Vídeo Python"
#print(frase.count("O")) # neste ex pedi para contar quantas vezes tema  letra "O" maiuscula, resultado: 0, mas se eu colocar um .upper()
#print(frase.upper().count("O")) # neste ex ele me diz resultado 3, pois joguei tudo para maiuslo e depois perguntei quantas tinham;

# frase = "Curso em Video Python"
# print(len(frase.strip())) #conta quantas espaços #já com o strip() remove os espaços antes e depois

# frase = "Curso em Vídeo Python"
# print(frase.replace("Python", "Android")) # ele iria substituir dentro da frase a palavra '"Python" por "Android"

# frase = "Curso em Vídeo Python"
# frase = frase.replace("Python", "Android")  # string são imultaveis, porém se usr uma atribuição ele é alterado
# print(frase)

# frase = "Curso em Vídeo Python"  # verificar se a palavra "curso" trá dentro da frase? true (verdadeiro)
# print("Curso" in frase)


# frase = "Curso em Vídeo Python"
# print(frase.find("Curso")) # diz a posição que "curso" começou, nete ex: apresenta o "0" (zero)


# frase = "Curso em Vídeo Python"
# print(frase.lower().find("vídeo")) #"lower transformou tudo de frasse em minusculo e logo find pergunta a posição que se inicia "vídeo" resultado 9

# frase = "Curso em Vídeo Python"
# print(frase.split())  #vai dividir em lista "Curso, em, Video, Python

frase = "Curso em Vídeo Python"
dividido = frase.split()
print(dividido[1][0])  # Solicitei que dentro de frase o .split() listasse a frase, depois pedi para pegar lista 2 (em) e falar qual a 3° letra mostra: "e"


