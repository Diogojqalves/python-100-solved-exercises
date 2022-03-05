while(True):
     n = int(input('Introduza o primeiro limite:'))
     if not n >= 0:
        print('Vamos calcular o factorial')
     else:
        break

#calcular fatorial
# n * n-1, ... n*1 = fatorial
if n == 0:
    print('%d! = 1' % n)
else:
    fatorial = n
    for x in range(n - 1, 1, -1):
        fatorial = fatorial * x
    print('%d! = %d' % (n, fatorial))

print('fim')
