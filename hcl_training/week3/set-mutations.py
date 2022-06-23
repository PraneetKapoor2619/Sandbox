n_A = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())) :
        command = input().strip().split()
        N = set(map(int, input().split()))

        if command[0] == "update" :
                A.update(N)
        elif command[0] == "intersection_update" :
                A.intersection_update(N)
        elif command[0] == "difference_update" :
                A.difference_update(N)
        elif command[0] == "symmetric_difference_update" :
                A.symmetric_difference_update(N)
print(sum(A))