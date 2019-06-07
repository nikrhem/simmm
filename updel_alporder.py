n,m=input().split()
p=0
if len(n)>len(m):
  n,m=m,n
i=0
while i<len(n):
  p+=(ord(m[i])-ord(n[i]))
  i+=1
for i in range(i,len(m)):
  p+=ord(m[i])-ord('a')+1
print(p)