'''
 Crie um programa que leia nomes do utilizador e termine quando for introduzido 
um nome repetido
'''
count = 0
lista = ''

while count < 1:
    teclado = str(input('introduza um nome:'))
    teclado = teclado.strip()
    nome = teclado.lower()
    lista = lista + ' ' + nome
    if lista.count(nome) > 1:
        count +=1
        print('Fim do programa')

