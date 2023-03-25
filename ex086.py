# CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO. NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMATAÇÃO CORRETA.
num = [[], [], [],
        [], [], [],
        [], [], []]
for c in range(0, 9):
    h = int(input(f"Digite o {c}° valor:"))
    if c == 0:
        num[0].append(h)
    elif c == 1:
        num[1].append(h)
    elif c == 2:
        num[2].append(h)
    elif c == 3:
        num[3].append(h)
    elif c == 4:
        num[4].append(h)
    elif c == 5:
        num[5].append(h)
    elif c == 6:
        num[6].append(h)
    elif c == 7:
        num[7].append(h)
    elif c == 8:
        num[8].append(h)
print(f'{num[0]}'.center(5), f'{num[1]}'.center(5),f'{num[2]}'.center(5))
print(f'{num[3]}'.center(5), f'{num[4]}'.center(5),f'{num[5]}'.center(5))
print(f'{num[6]}'.center(5), f'{num[7]}'.center(5),f'{num[8]}'.center(5))

# Como o profesor fez:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("=-" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()


#youtube fez:
# matriz = [[],[],[]]
# for l in range(0,3):
#         for c in range(0,3):
#                 matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
# print('-='*30)
# for l in range(0,3):
#         for c in range(0,3):
#                 print(f'[{matriz[l][c]:^5}]', end='')
#         print()
