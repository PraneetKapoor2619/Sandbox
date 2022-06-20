if __name__ == "__main__":
        N, M = map(int, input().split())
        athlete_data = [list(map(int, input().split())) for i in range(N)]
        K = int(input())
        athlete_data.sort(key = lambda x: x[K])
        for listing in athlete_data:
                for data in listing:
                        print(data, end = " ")
                print("")