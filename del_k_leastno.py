from itertools import combinations
a,n=map(str,input().split())
l=len(a)
n = int(n)
k=list(combinations(str(a),l-n))
k=(sorted(k))
print("".join(k[0]))