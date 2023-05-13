# 1043 - Triângulo

a,b,c = map(float, input().split())

if a+b>c and a+c>b and b+c>a:
    print(f'Perimetro = {(a+b+c):.1f}')
else:
    print(f'Area = {(0.50*(a+b)*c):.1f}')