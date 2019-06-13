p,q=map(int,input().split())
arr=list(map(int,input().split()))
temp=[]
for i in range(0,q):
    f=list(map(int,input().split()))
    l=f[0]
    for j in range(min(f)-1,max(f)):
        if l>arr[j]:
        	l=arr[j]
    temp.append(l)
for i in range(0,len(temp)):
    print(temp[i])