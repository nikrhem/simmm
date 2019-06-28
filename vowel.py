s = input()
x = [str(p) for p in s]
c=0
for i in range(0,len(x)):
	if(x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u' or x[i]=='A' or x[i]=='E' or x[i]=='I' or x[i]=='O' or x[i]=='U'):
		c+=1
if c!=0:
	print("yes")
else:
	print("no")