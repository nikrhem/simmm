arr = list()
n = int(input())
for i in range(0,n):
	a = input()
	arr.append(int(a))
print(arr)
arr.sort()
print(arr[n-1])