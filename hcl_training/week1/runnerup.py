if __name__ == '__main__':
        n = int(input())
        arr = map(int, input().split())
        arr = list(arr)
        score_set = sorted(set(arr), reverse=True)
        print(score_set[1])