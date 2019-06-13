import sys, string, math
def cnt_1(n) :
    p = bin(n)[2:]
    q = p.count('1')
    return q
n = int(input())
a1 = [ int(x) for x in input().split()]
a2 = []
for i in range(0,n) :
    a2.append((cnt_1(a1[i]),a1[i]))
a3 = sorted(a2, key=lambda x : (x[0],x[1]),reverse=True)
L = [x[1] for x in a3 ]
for i in range(0,len(L)) :
    print(L[i])