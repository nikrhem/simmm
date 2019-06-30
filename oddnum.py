n = input()
x = [int(x) for x in n]
c =[]
for i in range(0,len(x)):
	if x[i]%2!=0:
		c.append(x[i])
for i in range(0,len(c)):
	print(c[i],end=" ")