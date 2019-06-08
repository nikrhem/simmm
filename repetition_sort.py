n = int(input())
arr = list(map(int,input().split()))
rep = []
s= len(arr)
for i in range(s):
	k = i+1
	for j in range(k,s):
		if arr[i]==arr[j] and arr[i] not in rep:
			rep.append(arr[i])
rep.sort()
rep = [str(x) for x in rep]
print(" ".join(rep))