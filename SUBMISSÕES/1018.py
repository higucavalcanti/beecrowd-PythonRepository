# 1018 - Cédulas

valor = int(input())
while valor > 1000000:
    valor = int(input())

print(valor)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for i in cedulas:
    qtd_cedulas = int(valor / i)
    print(f'{qtd_cedulas} nota(s) de R$ {i},00')
    valor -= qtd_cedulas * i