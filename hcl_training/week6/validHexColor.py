import re

buffer = ""
for _ in range(int(input())) :

        buffer += input()

match = re.findall(r"#([0123456789abcdefABCDEF]{6}|[0123456789abcdefABCDEF]{3})(?=[^\n^ ^{])", buffer)

for number in match :
        print("#{:s}".format(number))