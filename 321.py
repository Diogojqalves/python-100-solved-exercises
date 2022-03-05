"""
Escreva um programa que leia 10 valores 
do utilizador e indique no fim se foi introduzido algum número 
divisível por 7.
"""

p = 10
div = False


while p > 0:
    num = int(input('introduza um nr: '))
    p -= 1
    if (num % 7) == 0:
        div = True

if div == True:
    print('foi introduzido pelo menos um numero divisivel por 7')  
else:
    print('n foi introduzido nenhum nr divisivel por 7')
    
