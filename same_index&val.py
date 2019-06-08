n = int(input())
arr = list(map(int,input().split()))
rep = []
for i in range(0,n):
	if arr[i]==i:
		rep.append(i)
rep.sort()
if(len(rep)!=0):
	rep = [str(x) for x in rep]
	print(" ".join(rep))
else:
	print("-1")