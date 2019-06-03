n = input()
a = num = 0
for i in n:
	if(i.isdigit()):
		num+=1
	elif(i.isalpha()):
		a+=1
if(num>1 and a>1):
	print("yes")
else:
	print("no")