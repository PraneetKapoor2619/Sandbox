from itertools import combinations

N = int(input())
LIST = sorted(input().split(" "))
K = int(input())

index_list = [n for n in range(1, len(LIST) + 1)]
combos = list(combinations(index_list, K))

sigma = 0
for combo in combos:
        for index in combo:
                if (LIST[index - 1] == 'a'):
                        sigma += 1
                        break
print(round(sigma / len(combos), 3))