# 1022 - TDA Racional

cases = int(input())
 
for i in range(0,cases):
    n1, b, d1, op, n2, b2, d2 = input().split(' ')
    n1, d1, n2, d2 = int(n1),int(d1),int(n2),int(d2)
    if op == "+":
        case1 = (n1 * d2 + n2 * d1)
        case2 = (d1 * d2)
    elif op == "-":
        case1 = (n1 * d2 - n2 * d1)
        case2 = (d1 * d2)
    elif op == "*":
        case1 = (n1 * n2)
        case2 = (d1 * d2)
    elif op == "/":
        case1 = (n1 * d2)
        case2 = (n2 * d1)
    def fat(n, m):
        if m == 0:
            return n
        else:
            return fat(m, n % m)
    print('{}/{} = {:.0f}/{:.0f}'.format(case1,case2, case1/fat(case1,case2),case2/fat(case1,case2)))