# 1045 - Tipos de Triângulos

n = input().split()
x, y, z = n

n1 = float(1); n2 = float(1); n3 = float(1)
x = float(x); y = float(y);z = float(z)

if x >= y and x >= z:
    n1 = x
    if y >= z:
        n2 = y;n3 = z
    else:
        n2 = z;n3 = y
if y >= x and y >= z:
    n1 = y
    if x >= z:
        n2 = x
        n3 = z
    else:
        n2 = z; n3 = x

if z >= x and z >= y:
    n1 = z
    if x >= y:
        n2 = x;n3 = y
    else:
        n2 = y;n3 = x             

if x == y and y == z:
    n1=x; n2=y; n3=z

x = n1; y = n2; z = n3

if x >= (y + z):
    print('NAO FORMA TRIANGULO')
else:
    if (x ** 2) == (y ** 2 + z ** 2):
        print('TRIANGULO RETANGULO')
    if (x ** 2) > (y ** 2 + z ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (x ** 2) < (y ** 2 + z ** 2):
        print('TRIANGULO ACUTANGULO')
    if (x == y == z):
        print('TRIANGULO EQUILATERO')
    if x == y != z or y == z != x or x == z != y:
        print('TRIANGULO ISOSCELES')
