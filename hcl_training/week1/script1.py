x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [el for el in [[i, j, k] if (i + j + k != n) else None for k in range(z + 1) for j in range(y + 1) for i in range(x + 1)] if el is not None]
result.sort()
print(result)