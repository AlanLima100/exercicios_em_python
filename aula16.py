lanche = ("hambúrguer", "suco", "pizza", "pudim", "batata Frita")
for comida in lanche: # Para cada comida em lanche ↓ - obs: esse não tem como mostrar a posição - maneira mais simples
    print(f"Eu vou comer {comida}")


for pos, comida in enumerate(lanche): # ele me dá tento os dados quanto a posição
    print(f"-Eu vou comer  {comida} na posição  {pos}")


for cont in range(0, len(lanche)): # vai começar na posição ( 0 zero) e vai até len(lanche) que neste exemplo é 0 1 2 3 4
    print(cont)

for cont in range(0, len(lanche)): # "cont" na posição (zero)
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")





print(sorted(lanche)) # vai mostrar lanche em ordem alfabetica [ ] como se tivesse mostrar em lista



a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c)) # vai me mostrar o tamanho dessa tupla


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))  # quantas vezes está aparecendo o número cinto (5) dentro de "c"


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(8)) # em que posição está o "8"


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(2)) # neste caso ele pega a primeira ocorrência vai mostrar na posição "3" (três) se eu quiser mostrar o da posição "4"

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(2, 4)) # vai mostrar o "2" começando da posição "4"


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1)) # mostrar o "5" (cinco) começando da posição "1" (um)

pessoa = ("Alan", 27, "M", 78.89)
print(pessoa)


pessoa = ("Alan", 27, "M", 78.89)
del(pessoa) # eu posso apagar uma tupla inteira, agora um objeto não posso.
print(pessoa)