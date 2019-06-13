import sys, string, math
np,kp = input().split()
np,kp = int(np), int(kp)
Li = [ int(x) for x in input().split()]
for i in range(0,kp) :
    u,v = input().split()
    u,v = int(u), int(v)
    print(sum(Li[u-1:v]))