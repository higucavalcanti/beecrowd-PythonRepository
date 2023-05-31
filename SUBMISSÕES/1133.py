# 1133 - Resto da Divisão

X= int(input())
Y= int(input())
if X > Y:
    a= Y
    b= X
elif X <= Y:
    a= X
    b= Y
for i in range(a+1, b):
    if i%5==2 or i%5==3:
        print(i)