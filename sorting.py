n=int(input())
a=list(map(int,input().split()))
a.sort()
arr = [str(x) for x in a]
print(', '.join(arr))
