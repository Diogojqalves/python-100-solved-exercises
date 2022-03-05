#Escreva um programa para imprimir os números inteiros entre 1
#e 10 na mesma linha, primeiro em ordem crescente e depois em
#ordem decrescente.

for x in range (1, 11):
    print(x, end=" ")

for x in range (10, 0, -1):
    print(x, end=" ")