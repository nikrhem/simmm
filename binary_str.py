def check_str(s):
	p = set(s)
	s = {'0','1'}
	if s==p or p=={'0'} or p=={'1'}:
		print("yes")
	else:
		print("no")
s = input()
check_str(s)