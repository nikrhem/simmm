n,k = (input()).split()
n = int(n)
k = int(k)
a= list(map(int,input().split()))
l=a.count(k)
if(l>0):
	print("yes")
else:
	print("no")