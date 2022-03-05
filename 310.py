"""
10) Escreva um programa para ler as notas de n alunos 
(sendo n introduzido pelo utilizador). As notas deverão 
estar entre 1 e 5. O programa deverá contar quantos alunos 
tiveram cada uma das notas possíveis.
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

# ler notas entre 1 e 5
i = 1
n1, n2, n3, n4, n5 = 0, 0, 0, 0, 0

while i <= n:
    entrada = input(f"Introduza a nota do aluno {i}: ")
    if entrada.isdigit():
        nota = int(entrada)
        if nota >= 1 and nota <= 5:
            i += 1
            if nota == 1:
                n1 += 1
            elif nota == 2:
                n2 += 1
            elif nota == 3:
                n3 += 1
            elif nota == 4:
                n4 += 1
            else:
                n5 += 1
        else:
            print("AVISO: A nota deve estar no intervalor de 1 e 5")
    else:
        print("AVISO: Só são permitidos valores núméricos")

print("Nota 1:", n1)
print("Nota 2:", n2)
print("Nota 3:", n3)
print("Nota 4:", n4)
print("Nota 5:", n5)
