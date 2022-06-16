N, X = map(int, input().split(" "))

marklist = []
for x in range(X):
        marklist.append(list(map(float, input().split(" "))))

compressed_marklist = zip(*marklist)
for marks in compressed_marklist:
        print(round(sum(list(marks)) / len(marks), 1))