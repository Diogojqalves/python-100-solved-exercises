'''
Crie um programa que leia o nome próprio do utilizador e imprima uma 
mensagem personalizada do tipo: "Olá João!"
'''
a = 'Olá'
nome = input('Indique o seu nome próprio: ')
print(a + ' ' + nome + '!')

'''
Altere o programa de modo a que se o nome for "Bartolomeu", o programa 
imprima "Dá cá o meu!".
'''

if nome == "Bartolomeu":
    print('Dá cá o meu!')

'''
Altere o programa anterior para que a mensagem surja para todos os nomes 
terminados em "eu". Exemplo:> Olá Zebedeu! Dá cá o meu!
'''
if nome[-1] == 'u' and nome[-2] == 'e':
    print('Dá cá o meu!')