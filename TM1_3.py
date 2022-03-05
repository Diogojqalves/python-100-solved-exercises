"""
A série de Fetuccine é gerada da seguinte forma: os dois primeiros termos são fornecidos pelo 
utilizador; a partir daí, os termos são gerados com a soma ou subtração dos dois termos anteriores de 
acordo com as seguintes regras: 

𝐴𝑖 = 𝐴𝑖−1 + 𝐴𝑖−2, 𝑝𝑎𝑟𝑎 𝑖 𝑖𝑔𝑢𝑎𝑙 𝑎 í𝑚𝑝𝑎𝑟
𝐴𝑖 = 𝐴𝑖−1 − 𝐴𝑖−2 , 𝑝𝑎𝑟𝑎 𝑖 𝑖𝑔𝑢𝑎𝑙 𝑎 𝑝𝑎𝑟

Crie um algoritmo que imprima os N primeiros termos da série de Fetuccine, sabendo-se que para 
existir esta série serão necessários pelo menos três termos.

"""

# ler primeiro termo a1
a = int(input("Digite o 1º termo da serie de Fetuccine -> "))
# ler segundo termo a2
b = int(input("Digite o 2º termo da serie de Fetuccine -> "))

# ler o numero de termos que se pretende visualizar
n = 0
while n < 2:
    n = int(input("Digite o nº de termos que pretende ver -> "))
    if n < 2:
        print("o nº de termos tem que ser maior ou igual a 2!")

# determinar e imprimir os elementos da serie
print(a, b, end=" ")
i = 3 # numero do termo (Ai)
ai = 0 # var com valor de Fetuccine em i

while i <= n:
    if i % 2 != 0: # se i é impar
        ai = b + a
    else: # se i é par
        ai = b - a

    print(ai, end=" ")
    a = b
    b = ai
    i += 1