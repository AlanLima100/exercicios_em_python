# Escreva um programa qe leia um valor em metros e o exiba convertido em centimetros e milímetros.
m = float(input("Digite seu valor em metros:"))
c = m * 100
mi = m * 1000
print("O valor de {} convertido para centimetro é: {}cm e o valor de {} convertido para milimetro é {} mm".format( m, c, m, mi))
