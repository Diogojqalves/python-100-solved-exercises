'''
 Crie um programa que imprima um número de 4 dígitos invertido 
(ex. 4536 -> 6354)
'''
while True:
    Nr = int(input("introduza um nr inteiro de 4 digitos: "))
    if Nr > 999 and Nr < 10000:
        break  


inverso = 0    
while(Nr > 0):    
    resto = Nr % 10    
    inverso = (inverso *10) + resto # multiplicar primero nr por 10 para ficar na esquerda
    Nr = Nr // 10    
     
print("\n inverso do nr introduzido = %d" % inverso)  