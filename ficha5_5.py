from random import randint

TAM = 20
a, b = 1, 50
v = []

for x in range (0, TAM):
    v.append(randint(a, b))

print(v)

maior = v[0]
segMaior = -1

for x in range (1, TAM):
    if v[x] > maior:
        segMaior = maior
        maior = v[x]
    else:
        if v[x] > segMaior and v[x] < maior:
            segMaior = v[x]

print(segMaior)
print(f'{maior} é o maior')