#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM POLÍNDROMO, DESCONSIDERANDO OS ESPAÇOS.

pa = str(input("Dgitei uma frase:")).strip().upper()
pu = pa.split()
junto = "".join(pu)
inverte = junto[::-1]

if inverte == junto:
    print("\033[32m{} é uma palavra PALÍNDROMO".format(pa))
else:
    print("\033[31m{} NÃO É uma palavra POLÍNDROMO".format(pa))

# PROFESSOR:

pa = str(input("Dgitei uma frase:")).strip().upper()
pu = pa.split()
junto = "".join(pu)
inverso =""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print("Temos um Pal[indromo!")
else:
    print("A frase digitada não é um palíndromo!")





# PROFESSOR:



pa = str(input("Dgitei uma frase:")).strip().upper()
pu = pa.split()
junto = "".join(pu)
inverso = junto[::-1]

if inverso == junto:
    print("Temos um Pal[indromo!")
else:
    print("A frase digitada não é um palíndromo!")



























