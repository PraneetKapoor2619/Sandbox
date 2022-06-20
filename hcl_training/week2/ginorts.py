string = [ch for ch in input()]
combined = []
combined.append(sorted([ch for ch in string if ch.islower()]))
combined.append(sorted([ch for ch in string if ch.isupper()]))
combined.append(sorted([n for n in string if n.isdigit() and int(n) % 2 == 1]))
combined.append(sorted([n for n in string if n.isdigit() and int(n) % 2 == 0]))
result = ""
for i in combined:
        if (len(i) > 0):
                result += "".join(i)
print(result)