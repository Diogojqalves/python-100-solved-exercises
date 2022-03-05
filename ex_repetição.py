#ler limites
p = 2
while p > 0:
  if p == 2:
      a = int(input('Introduza o primeiro limite:'))
      if a > 0:
          p = p - 1
      else:
              print('Aviso: o número tem de ser maior que zero, tente novamente')
  if p == 1:
      b = int(input('Introduza o primeiro limite:'))
      if b > 0 and b != a:
          p = p - 1
      else:
              print('Aviso: o número tem de ser maior que zero e diferente de %d, tente novamente' % a)

#determinar limite inferior e superior
minimo = a
maximo = b
if a > b:
    minimo = b
    maximo = a

#mostrar intervalo e respetiva soma na consola
somaIntervalo = 0
for x in range(minimo, maximo + 1):
    print(x, end='')
    somaIntervalo += x 

print("\n Soma do intervalo de valor: %d" %somaIntervalo)