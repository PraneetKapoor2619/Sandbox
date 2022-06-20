from itertools import permutations

string = input().split(" ")
limit = int(string[1])
string = string[0]

perms = list(permutations(string, limit))
perms.sort()
for perm in perms:
        formatted_output = "".join(perm)
        print(formatted_output)