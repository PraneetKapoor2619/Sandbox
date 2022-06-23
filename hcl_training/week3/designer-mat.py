odd = lambda i : ((2 * i) - 1)

if __name__ == "__main__" :
        N, M = map(int, input().split())
        centerline = int((N + 1) / 2)
        mat = []
        for n in range(1, centerline + 1) :
                if (n == centerline) :
                        mat += ["-" * int((M - 7) / 2) + \
                        "WELCOME" + \
                        "-" * int((M - 7) / 2)]
                else :
                        mat += ["-" * int((M - (3 * odd(n))) / 2) + \
                        ".|." * odd(n) + \
                        "-" * int((M - (3 * odd(n))) / 2)]
        mat += mat[-2::-1]
        for line in mat :
                print(line)