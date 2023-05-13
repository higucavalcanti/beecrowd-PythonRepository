# 1042 - Sort Simples

saida = input().split()

valores = [int(i) for i in saida]

valores.sort()

print(*valores, sep='\n')
print()
print(*saida, sep='\n')