n,k = (input()).split()
n = int(n)
k = int(k)
if(k>n):
	for i in range(n,k+1):
		if(i%2==0):
			print(i)