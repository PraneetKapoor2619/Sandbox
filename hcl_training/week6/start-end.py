import re

S = input()
k = input()

match_list = re.finditer(r"(?=(%s))" % (k), S)

flag = False

for match in match_list :
        flag = True
        print((match.start(1), match.end(1) - 1))

if flag == False : print((-1, -1))