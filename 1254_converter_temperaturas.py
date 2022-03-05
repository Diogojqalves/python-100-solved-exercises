
# dados de entrada
tempF = float(input("Digite a tempreratura em graus Fahrenheit -> "))

# converter para graus Celsius
tempC = (tempF - 32) / 1.8

# apresentar resultados
print("%.2fºF => %.2fºC" %(tempF, tempC))