n = int(input())
k = int(input())
if(k>n):
	for i in range(n,k+1):
		if(i%2!=0):
			print(i)
		