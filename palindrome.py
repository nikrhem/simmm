a = int(input())
temp = a
s = 0
while(temp>0):
	r = temp % 10
	s = s * 10 + r
	temp = temp//10
if (a==s):
	print("yes")
else:
	print("no")