a,n = (input()).split()
a= int(a)
n= int(n)
for i in range(a,n):
  temp = i
  s = 0
  while(temp>0):
    r=temp%10
    s= s + (r*r*r)
    temp = temp//10
  if(i==s):
    print(i)