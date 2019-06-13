p,q=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(0,q):
	u,v=map(int,input().split())
	q=arr[u-1:v]
	for j in q:
		c=c^j
	print(c)
	c=0