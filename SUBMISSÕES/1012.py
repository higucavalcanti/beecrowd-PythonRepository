# 1012 - Área

A,B,C = [float(x) for x in input().split()]
t = (A*C)/2
print('TRIANGULO:','{:.3f}'.format(t))
pi = 3.14159
c = pi * (C**2)
print('CIRCULO:','{:.3f}'.format(c))
trap = ((A+B) * C)/2
print('TRAPEZIO:','{:.3f}'.format(trap))
q = B**2
print('QUADRADO:','{:.3f}'.format(q))
r = A*B
print('RETANGULO:','{:.3f}'.format(r))