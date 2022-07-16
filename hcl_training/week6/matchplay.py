import re

m = re.match(r"(\S+)@(\w+)\.(\w+)", "kapoorpraneet2619@gmail.com")

print(m.groups())