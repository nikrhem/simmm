n = input()
a = len(n)
x = [str(x) for x in n]
if a%2==0:
	p = a/2
	x[int(p)-1]='*'
	x[int(p)]='*'
else:
	p = (a+1)/2
	x[int(p)-1]='*'
for i in range(0,a):
	print(x[i],end="")