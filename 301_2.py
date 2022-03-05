#Escreva um programa para imprimir os números inteiros entre 1
#e 10 na mesma linha, primeiro em ordem crescente e depois em
#ordem decrescente.

#2 solução

x = 1
while x <= 10:
    print(x, end=" ")
    x+= 1
print()


x= 10
while x >= 1:
    print(x, end=" ")
    x -= 1