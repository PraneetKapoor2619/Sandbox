n, m = map(int, input().split())

arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for element in arr :
        if element in A :
                happiness += 1
        elif element in B :
                happiness += (-1)
        else :
                continue
print(happiness)