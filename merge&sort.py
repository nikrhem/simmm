n = int(input())
x = []
for i in range(0,n):
	li=list(map(int,input().split()))
	x.append(li)
m=[]
for i in x:
	for j in i:
		m.append(j)
m.sort()
for i in m:
	print(i,end=" ")