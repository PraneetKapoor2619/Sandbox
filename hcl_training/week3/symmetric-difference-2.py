n = int(input())
set_english = set(map(int, input().split()))
b = int(input())
set_french = set(map(int, input().split()))

print(len(set_english.symmetric_difference(set_french)))