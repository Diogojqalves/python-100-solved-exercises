# Escreva um programa que some os algarismos de um número

n=int(input("Enter a number:"))

tot=0

while(n>0):
    dig = n % 10
    tot = tot + dig
    n = n //10
print("The total sum of digits is:",tot)