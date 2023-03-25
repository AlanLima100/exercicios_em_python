#p = str(input("Digite algo:"))
#print(p)

#p = float(input("Digite algo:"))
#print(type (p))

#p = bool(input("Digite algo:"))
#print(type (p))

n = input("Digite algo:")
#print(n.isnumeric()) # o que for digitado dentro de algo quer saber se é número
#print(n.isalnum()) # PRA SABER SE TEM LETRAS E NÚMERO
#print(n.isupper()) # PRA SABER SE TEM APENAS LETRAS MAIUSCULAS
# print( "O tipo primitivo desse valor é", type(n))
# print(" Só tem espaços?",n.isspace())
# print("É um número?",n.isnumeric())
# print("É alfabético?", n.isalpha())
# print("É alfanúmerico?", n.isalnum())
# print("Está em maiusculas?", n.isupper())
# print("Está em minusculas?", n.islower())
# print("Está capitalizada", n.istitle()
print("o tipo primito desse valor é:", type(n), "Só tem espaços?{0}",n.isspace(), "É umm número? {1}", n.isnumeric(), "É Alfabético? {2}",n.isalpha(),"É alfanúmerico?{3}", n.isalnum(),
      "Está em maiusculas?c{4}", n.isupper(), "Está em minusculas? {5}", n.islower(), "Está Capitalizada? {6}", n.istitle().__format__(n))



