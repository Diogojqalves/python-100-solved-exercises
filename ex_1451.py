a = int(input('Introduza um número inteiro:'))
b = int(input('Introduza o divisor:'))

def division(numerator,denominator):
    if denominator == 0:
        raise ZeroDivisionError
    fraction  = 0
    while numerator >= denominator:
          numerator = numerator - denominator
          fraction  = fraction + 1
    return (fraction, numerator)   