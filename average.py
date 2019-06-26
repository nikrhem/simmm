n=int(input())
a=list(map(int,input().split()))
avg=int(n/2)
l1=a[:avg]
l2=a[avg::]
if ((sum(l1)//len(l1))==(sum(l2)//len(l2))):
    print("yes")
else:
    print("no")