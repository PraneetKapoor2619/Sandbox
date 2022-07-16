import re

S = input()

match_list = re.findall(r"([a-zA-Z0-9])\1+", S) 

if len(match_list) > 0 :
        print(match_list[0][0])
else :
        print(-1)