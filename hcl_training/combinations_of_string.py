from itertools import combinations

S = input().split(" ")
K = int(S[1])
S = sorted([ch for ch in S[0]])

megacombo = [list(combinations(S, k)) for k in range(1, K + 1)]
for minicombo in megacombo:
        for combo in minicombo:
                combo = "".join(combo)
                print(combo)