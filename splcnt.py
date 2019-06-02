import re
string = input()
specialChars = len(string) - len(re.findall('[\w]', string) )
print(specialChars)