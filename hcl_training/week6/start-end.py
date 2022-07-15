import re

S = input()
k = input()
m = re.findall(r'(?<=a)(%s)' % (k), S)
print(m)