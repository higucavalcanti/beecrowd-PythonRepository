# 1101 - Sequência de Números e Soma

menor = 0
maior = 0
aux = 0

cond = True
while cond:
        v1, v2 = map(int, input().split())
   
        if(v1 <= 0 or v2 <= 0):
                break

        menor = v2 if v2 < v1 else v1
        maior = v1 if v1 > v2 else v2
        
        if maior > menor :
                aux = maior
                maior = menor
                menor = aux
               
        soma = 0
       
        while maior <= menor :
         print(maior, end=' ')
         soma += maior
         maior+=1
        print("Sum=%d"%soma)