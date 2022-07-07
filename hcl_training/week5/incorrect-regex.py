import re

for _ in range(int(input())) :
        try :
                regex = input()
                result = re.compile(regex)
                print("True")
        except re.error :
                print("False")