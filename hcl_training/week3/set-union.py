n = int(input())
set_english = set(map(int, input().split()))
b = int(input())
set_french = set(map(int, input().split()))

total_number = len(set_english.union(set_french))
print(total_number)