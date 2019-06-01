arr = list()
n = int(input())
for i in range(0,n):
	a = input()
	arr.append(int(a))
arr.sort()
print(arr[0])