def xor_sum(x):
    global A
    result = 0
    for i in range(0, len(A)):
        result += (x ^ A[i])
    return result

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    A = []
    for i in range(0, N):
        A.append(int(input()))

    _max = 0
    _val = 0
    for x in range(0, K + 1):
        result = xor_sum(x)
        if (result > _max):
            _max = result
            _val = x
    print(_max)
