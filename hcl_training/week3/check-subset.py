for _ in range(int(input())) :
        n_a, A = int(input()), set(map(int, input().split()))
        n_b, B = int(input()), set(map(int, input().split()))
        print(A.issubset(B))