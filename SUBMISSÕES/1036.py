# 1036 - Fórmula de Bhaskara

import math

conta = input().split()
a = float(conta[0])
b = float(conta[1])
c = float(conta[2])

delta = b * b - 4 * a * c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    x1 = (-b + math.sqrt(delta))/(2 * a)
    x2 = (-b - math.sqrt(delta))/(2 * a)
    print("R1 = %0.5f" % x1)
    print("R2 = %0.5f" % x2)