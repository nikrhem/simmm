a,b = input().split()
a = int(a)
b = int(b)
for i in range(a+1,b):
	for j in range(2,i):
		if(i%j==0):
			break
	else:
		print(i,end=' ')