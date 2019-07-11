import math
n = float(input())
n = math.ceil(n)
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if n<26:
  for i in range(0,n):
    k=0
    while k<=i:
      print(a[k],end=" ")
      k+=1
    print("\n")
  for i in range(n-2,-1,-1):
    for j in range(0,i+1):
      print(a[j],end=" ")
    print("\n")
else:
  print("Enter n less than or equal to 26")