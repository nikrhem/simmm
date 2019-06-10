n = int(input())
arr = list(map(int,input().split()))
c = 0
s = len(arr)
for i in range(s-2):
	for j in range(i+1,s-1):
		for k in range(j+1,s):
			if arr[i]<arr[j]<arr[k] and i<j<k:
				c+=1
print(c)