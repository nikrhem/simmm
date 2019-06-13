n=int(input())
arr=list(map(int,input().split()))
c=[1]*n
for i in range(n):
    if i==0:
        if arr[i]>arr[i+1]:
            c[i]=c[i]+c[i+1]
    elif i>0:
        if arr[i]>arr[i-1]:
            c[i]=c[i]+c[i-1]
print(sum(c))