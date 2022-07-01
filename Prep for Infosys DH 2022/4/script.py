def base_convert (M, base):
    result = []
    while (M >= base):
        rem = M % base
        M = M // base
        result.insert(0, rem)
    result.insert(0, M)
    return result

def check_digits(result):
    if (len(result) == 0) :
        return False
    prev = result[0]
    for i in range(1, len(result)):
        if (result[i] == prev):
            prev = result[i]
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    M = int(input())
    base = 2
    while (True):
        if (check_digits(base_convert(M, base)) == True):
            break
        else:
            base += 1
    print(base)
