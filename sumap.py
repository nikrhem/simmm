n,a,d = (input()).split()
n = int(n)
a = int(a)
d = int(d)
sum = 0
i = 0
while i<n:
  sum = sum+a
  a = a+d
  i = i+1
print(sum)