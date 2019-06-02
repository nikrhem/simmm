string =input()
count = 0
for c in string:
  if c.isnumeric()!=False:
    count = count+1
print(count)