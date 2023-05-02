# 1010 - Cálculo Simples

linha = input().split()
c1 = int(linha[0])
n1 = int(linha[1])
v1 = float(linha[2])

linha = input().split()
c2 = int(linha[0])
n2 = int(linha[1])
v2 = float(linha[2])

vt = (n1*v1 + n2*v2)
print('VALOR A PAGAR: R$', '{:.2f}' .format(vt))