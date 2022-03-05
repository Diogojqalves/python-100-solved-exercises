"""
Um aluno do ISMAI já terminou N disciplinas com notas entre 10 e 20. Escreva um algoritmo que calcule 
a média das N notas e se a média for inferior a 13.5 escreve Suficiente, se for maior ou igual a 13.5 e 
inferior e 17.5 escreve Bom e se for superior ou igual a 17.5 escreve Muito Bom.
"""

n = int(input('nr de notas: '))
count = n
total = 0

while n > 0:
     nota = int(input('introduza a sua nota: '))
     if nota < 10:
         print('apenas notas entre 10 e 20 são válidas')
     if nota >= 10:
         total = total + nota
         n -= 1

media = total / count

if media < 13.5:
    print('%.1f = Suficiente' % (media))
if (media >= 13.5) and (media < 17.5):
    print('%.1f = Bom' % (media))
if media >= 17.5:
    print('%.1f = Muito Bom' % (media))