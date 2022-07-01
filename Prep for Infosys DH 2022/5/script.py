n = int(input())
m = int(input())
k = int(input())
arr = [0] * n
for i in range(0, m):
    tmp = int(input())
    arr[tmp - 1] = 1
count = 0
max_count = 0
pseudo_k = k
for i in range(0, n):
    if (arr[i] == 0):
        count += 1
    else:
        if (pseudo_k > 0):
            pseudo_k -= 1
            count += 1
        else:
            pseudo_k = k
            count = 0
    if (count > max_count):
        max_count = count
print(max_count)
