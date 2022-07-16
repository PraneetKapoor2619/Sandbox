import re

for _ in range(int(input())) :
        number = input()
        result = bool(re.match(r"^([789])([0-9]{9})$", number))
        if result == True : print("YES")
        elif result == False : print("NO")