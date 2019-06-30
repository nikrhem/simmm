n = int(input())
temp = n
for i in range(1,n+1):
	if temp%i==0:
		print(i,end=" ")