n = int(input())
a = list(map(int,input().split()))
temp = 0
for i in range(0,n):
	for j in range(0,i):
		if a[j]<a[i]:
			temp = temp+a[j]
print(temp)