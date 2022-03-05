'''
Escreva um programa que preencha um vetor de 20 posições com
os primeiros 20 números primos.
'''
vetor = []
count = 0
ePrimo = True

while count < 20:
    for x in range (2, 100):
        for i in range(2, int(x/2)+1):
            if (x % i) == 0:
                break
        else:
         if count < 20:
             vetor.append(x)
             count +=1
print(vetor)
          