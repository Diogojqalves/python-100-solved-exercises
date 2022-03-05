"""
13) [utilização de flags (ou não…)]. Escreva um programa que leia 
n números (sendo n introduzido pelo utilizador) e indique se os 
números são todos pares, se são todos ímpares ou se há ambos os 
tipos.
"""
n = 0
while n <= 0:
    entrada = input("Quantos alunos deseja introduzir: ")
    if entrada.isdigit():
        n = int(entrada)
        if n <= 0:
            print("AVISO: Tem de introduzir pelo menos 1 aluno.")
    else:
        print("AVISO: Só são permitidos valores núméricos")


i = 1
totalPares = 0
# pares = False
# impares = False

while i <= n:
    entrada = input(f"Introduza o número {i} de {n}: ")
    if entrada.isdigit():
        num = int(entrada)
        if num % 2 == 0:
            # pares = True
            totalPares += 1
        #else:
            #impares = True
        i += 1
    else:
        print("AVISO: Só são permitidos valores núméricos")


if totalPares == 0:
    print("São todos impares")
elif totalPares == n:
    print("São todos pares")
else:
    print("Total de pares: ", totalPares)
    print("Total de impares: ", (n - totalPares))