M = int(input())
set_M = set(map(int, input().split()))
N = int(input())
set_N = set(map(int, input().split()))

for integer in sorted(list(set_M.symmetric_difference(set_N))) :
        print(integer)