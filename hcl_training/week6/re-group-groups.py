import re

S = "..12345678910333111213141516171820212223"
match_list = re.findall(r"([a-zA-Z0-9])\1+", S) 
print(match_list)

match = re.match(r"([.a-zA-Z0-9])\1+", S)
try :
        print(match.groups())
except :
        print(None)