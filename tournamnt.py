n = int(input())
k = 1000
for i in range(0,20):
	if pow(2,i)<=n:
		a = abs(pow(2,i)-n)
		if a<=k:
			k=a
print(k)