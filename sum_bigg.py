n = int(input())
q = list(map(int,input().split()))
a = []
b = []
for i in range(len(q)):
	if i%2==0:
		a.append(q[i])
	else:
		b.append(q[i])
d = sum(a)
f = sum(b)
if d>f:
	print(d)
else:
	print(f) 