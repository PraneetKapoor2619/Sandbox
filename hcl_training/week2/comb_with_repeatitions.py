from itertools import combinations_with_replacement

S = input().split(" ")
k = int(S[1])
S = sorted(S[0])

combos = list(combinations_with_replacement(S, k))
for combo in combos:
        combo = "".join(combo)
        print(combo)