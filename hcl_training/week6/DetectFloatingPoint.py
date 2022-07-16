import re

def isvalidfloat(N):

        if (re.match("^[+-]\.[0-9]+$", N) or \
        re.match("^.[0-9]+$", N) or \
        re.match("^[+-][0-9]+\.[0-9]+$", N) or\
        re.match("^[0-9]+\.[0-9]+$", N)) != None:
                return True
        else :
                return False

for _ in range(int(input())) :
        N = input()
        print(isvalidfloat(N))