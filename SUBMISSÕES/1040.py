# 1040 - Média 3

n1, n2, n3, n4 = input().split(' ')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

conta = (n1*2 + n2*3 + n3*4 + n4)/10

if(conta >= 7.0):
    print('Media: %.1f' %conta)
    print('Aluno aprovado.')
elif(conta<5.0):
    print('Media: %.1f' %conta)
    print('Aluno reprovado.')
else:
    print('Media: %.1f' %conta)
    print('Aluno em exame.')
    pf = float(input())
    print('Nota do exame: %.1f' %(pf))
    conta2 = (pf + conta)/2
    if(conta2>=5.0):
        print('Aluno aprovado.')
        print('Media final: %.1f' %(conta2))
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f' %(conta2))