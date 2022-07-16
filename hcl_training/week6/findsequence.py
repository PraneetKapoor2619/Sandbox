import re

match = re.search(r"(?<=\w)(a{2})(?=\w)", "Jaackaas")
print(match.groups())

match_list = re.finditer(r"(?<=a)?(a{2})(?=a)?", "Jaaaackaaas")
for match in match_list :
        print(match.start(1), match.end(1))