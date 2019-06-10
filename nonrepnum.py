a = int(input())
l = list(map(int,input().split()))
for x in l:
	if l.count(x)==1:
		print(x)