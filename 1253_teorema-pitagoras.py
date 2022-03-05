from math import sqrt

# vamos assumir que é um triangulo retangulo
# variaveis de entrada
# ler catetos 
a = int(input("Digite o cateto 1 -> "))
b = int(input("Digite o cateto 2 -> "))

# determinar a hipotenusa c^2 = a^2 + b^2
c = sqrt(a**2 + b**2)

# apresentar resultados
print("Hipotenusa -> %.3f" %c)
