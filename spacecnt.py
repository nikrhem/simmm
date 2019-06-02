string =input()
count = 0
for c in string:
  if c.isspace()!=False:
    count = count+1
print(count)