# 1019 - Conversão de Tempo

e = int(input())
h = e//3600
r = e%3600
m = r//60
s = r%60
print(str(h)+":"+str(m)+":"+str(s))