'''
Crie um programa que indique qual de três strings introduzidas pelo utilizador 
tem um comprimento superior.
'''

pri = str(input('Introduza um nome: '))
seg = str(input('Introduza um nome: '))
ter = str(input('Introduza um nome: '))

if len(pri) > len(seg) and len(pri) > len(ter):
    print(f'{pri} tem um comprimento superior')
elif len(seg) > len(pri) and len(seg) > len(ter):
    print(f'{seg} tem um comprimento superior')
else:
    print(f'{ter} tem um comprimento superior')