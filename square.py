import math
n,m = map(int,input().split())
num = n*m
r = math.sqrt(num)
if (r)**2==num:
	print("yes")
else:
	print("no")
