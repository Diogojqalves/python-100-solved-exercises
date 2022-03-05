
# ler variaveis de entrada peso e altura
peso = float(input("Introduza o seu peso (kg) -> "))
altura = float(input("Introduza a sua altura (m) -> "))

# calcular indice de massa corporal e guardar na variavel de saida -> imc
imc = peso / altura**2

# apresentar resultados
print("IMC = %.2f / %.2f^2 = %.2f" %(peso, altura, imc))


