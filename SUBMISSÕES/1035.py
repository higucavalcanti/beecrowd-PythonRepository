# 1035 - Teste de Seleção 1

valores_lidos = input()

valores_int = [int(x) for x in valores_lidos.split(' ')]
a = valores_int[0]
b = valores_int[1]
c = valores_int[2]
d = valores_int[3]

valido = b > c

valido = valido and d > a

valido = valido and c + d > a + b

valido = valido and c > 0 and d > 0

valido = valido and a % 2 == 0

if valido:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')