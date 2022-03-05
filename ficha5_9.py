'''
Crie um programa que leia 10 números float, coloque-os num vetor
e calcule a sua média.
'''
vetor = []
count = 1
total = 0
while count < 10:
    num = float(input('Introduza um nr float: '))
    total = num + total
    vetor.append(num)
    count += 1

media = total / 10
print('media = %.2f' % media)