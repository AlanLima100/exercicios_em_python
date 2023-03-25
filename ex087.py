# APRIMORE O DESAFIO ANTERIOR, mostrando no final:
 # A) A SOMA DE TODOS OS VALORES PARES DIGITADOS.
 # B) a SOMA DOS VALORES DA TERCEIRA COLUNA.
 # C) O MAIOR VALOR DA SEGUNDA LINHA.
valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = []
segundalinha = terceiracoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("=-" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{valores[l][c]:^5}]", end="")
    print()
for l in range(0, 3):
    for c in range(0, 3):
        if valores[l][c] % 2 == 0:
            soma.append(valores[l][c])
c = sum(soma)
print(f" A Soma de todos os valores pares digitados é {c}")
for l in range(0, 3):
    terceiracoluna = terceiracoluna + valores[l][2]
print(f"A soma dos valores da terceira coluna é {terceiracoluna}")
for c in range(0, 3):
    if c == 0:
        segundalinha = valores[1][c]
    elif valores[1][c] > segundalinha:
        segundalinha = valores[1][c]
print(f"O maior valor da seunga linha é {segundalinha}")







