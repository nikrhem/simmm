num_arr = list()
m=0
n = input()
for i in range(int(n)):
	a = input("n:")
	num_arr.append(int(a))
print(num_arr)
k = int(input())
for i in range(0,k):
	m=m+num_arr[i]
print(m)