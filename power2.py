n = int(input())
if n==1:
	print(n*2)
else:
	for i in range(0,n):
		if((2**i)>n):
			print(2**i)
			break
