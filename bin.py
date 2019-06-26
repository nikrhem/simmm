n=int(input())
al=[]
m=bin(2**n-1)[2::]
l=len(m)
for i in range(0,2**n):
	p=bin(i)[2::]
	if len(p)<l:
		al.append([p.count("1"),(l-len(p))*"0"+p])
	else:
		al.append([p.count("1"),p])
al.sort()
for i in range(0,len(al)):
	print(al[i][1])