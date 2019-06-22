ni,mi=map(int,input().split())
tem=[]
x=0
for i in range(ni):
    tem.append(list(map(int,input().split())))   
for i in range(ni):
    for j in range(mi-1):
        for k in range(j+1,mi+1):
            if tem[i][j:k]==[1]*len(tem[i][j:k]):
                 if all(tem[p+i][j:k]==[1]*len(tem[p+i][j:k]) for p in range(len(tem[i][j:k])-1)):
                     if len(tem[i][j:k])>x:
                        x=len(tem[i][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for i in range(x):
    print(*[1]*x) 