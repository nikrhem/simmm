n,o,m=map(str,input().split())
n = int(n)
m = int(m)
if o=='/':
	print(int(n/m))
elif o=='%':
	print(int(n%m))
else:
	print("error")