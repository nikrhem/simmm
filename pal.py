def reve(s):
	return(s[::-1])
s = input()
rev = reve(s)
if s == rev:
	print("yes")
else:
	print("no")