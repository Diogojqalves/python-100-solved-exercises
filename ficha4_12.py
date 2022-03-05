'''
Crie uma função que receba três inteiros como argumentos (ano, 
mês, dia) e verifique se se trata de uma data válida. O ano deverá 
estar entre 1900 e o presente ano. Deverá retornar um valor
booleano
'''

def data(ano, mes, dia):
    if ano > 1899 and ano < 2023:
        if mes > 0 and mes < 13:
            if dia > 0 and dia < 31:
                return True
    else:
        return False


a = int(input('Introduza o ano: '))
b = int(input('introduza o mes: '))
c = int(input('Introduza o dia: '))

print(data(a,b,c))