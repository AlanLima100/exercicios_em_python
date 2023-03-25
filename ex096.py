#FAÇA UM PROGRAMA QUIE TENHA UMA FUNÇÃO CHAMA ÁREA( ), QUE RECEBA AS DIMENSÕES DE UM TERRRENO RETANGULAR ( LARGURA E COMPRIMENTO ) E MOSTRE A ÁREA DO TRERRENO
def área(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg} x {comp} é de {a} m².")


print("Controle de Terrenos")
print("-=" * 30)
l = float(input("Largura (m): "))
c = float(input("COMPRIMENTO (m):"))
área(l, c)
