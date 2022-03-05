'''
Crie uma função que receba 2 notas (F1 e F2) de um aluno e 
retorne um booleano indicando se o aluno passou. Para passar, a 
soma das notas deve ser igual ou superior a 19 e ambas devem ser 
superiores a 7
'''
pt = int(input('nota de pt: ' ))
mat = int(input('nota de mat: '))
def notas(f1, f2):
    if (f1 > 7) and (f2 > 7) and (f1 + f2 > 18):
        return True
    else: 
        return False

notas(pt, mat)

print(notas(pt, mat))