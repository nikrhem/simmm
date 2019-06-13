n,k = map(int,input().split())
arr = list(map(int,input().split()))
c = 0
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		if (arr[i]+arr[j]==k):
			c+=1
			break
if(c):
	print("yes")
else:
	print("no")

