nik = int(input())
al = list(map(int,input().split()))
pm = 0
i=0
while i<len(al)-1:
	count = 0
	while i<len(al)-1 and al[i]<al[i+1]:
		count+=1
		i+=1
	if count>pm:
		pm = count
	i+=1
print(pm+1)
