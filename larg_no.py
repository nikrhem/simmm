n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse = True)
arr = [str(x) for x in arr]
print("".join(arr))