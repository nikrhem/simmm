n = int(input())
a = list(map(int,input().split()))
p = 0
i=0
while i<len(a)-1:
	count = 0
	while i<len(a)-1 and a[i]<a[i+1]:
		count+=1
		i+=1
	if count>p:
		p = count
	i+=1
print(p+1)
