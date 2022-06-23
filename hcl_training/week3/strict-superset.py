A = set(map(int, input().split()))
result = False
for _ in range(int(input())) :
        B = set(map(int, input().split()))
        if (A != B) and (A.issuperset(B)) :
                result = True
                continue
        else :
                result = False
                break
print(result)