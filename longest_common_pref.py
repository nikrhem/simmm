n=int(input())
arr=[]
for i in range(0,n):  
    w=input()
    arr.append(w)
l=[]
for i in zip(*arr):
    if i.count(i[0])==len(i): 
        l.append(i[0])
    else:
        break
print(''.join(l))
