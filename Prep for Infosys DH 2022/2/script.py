def combinations(array, tmp, sp, N):
    global max_xor
    for i in range(sp, N):
        tmp.append(array[i])
        if (len(tmp) > N/2):
            tmp.pop()
            return 
        else:
            z = 0
            for j in range(0, len(tmp)):
                z ^= tmp[j]
            if (z > max_xor):
                max_xor = z
            combinations(array, tmp, i + 1, N)
            tmp.pop()

if __name__ == "__main__":
    N = int(input())
    array = []
    for i in range(0,N):
        tmp = int(input())
        array.append(tmp)
    max_xor = 0
    combinations(array, [], 0, N)
    print(max_xor)
