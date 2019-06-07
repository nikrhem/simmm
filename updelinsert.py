a,b=input().split()
n=abs(len(a)-len(b))
for i in range(len(a)):
    if len(b)==1 and b[i] in a:
        break
    if a[i]!=b[i]:
        n+=1
print(n)