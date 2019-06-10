import math
import functools
n,q = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(q):
	l,m = map(int,input().split())
	a = functools.reduce(math.gcd,arr[l-1:m])
	print(a)