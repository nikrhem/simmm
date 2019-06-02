n,k = (input()).split()
n = int(n)
k = int(k)
for i in range(n+1,k):
	for j in range(2,i):
		if(i%j==0):
			break
		else:
			print(i,end=" ")