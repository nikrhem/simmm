a = int(input())
s = 0
temp = a
while(temp>0):
  r=temp%10
  s= s + (r*r*r)
  temp = temp//10
if(a==s):
  print("yes")
else:
  print("no")