from functools import reduce

for _ in range(int(input())) :
        n = int(input())
        array = list(map(int, input().split()))

        flag = bool()
        if (n == 1) :
                flag = True
        else :
                flag = False
                left_sum, right_sum = int(), int()

                for i in range(0, n - 1) :
                        if (i == 0) :
                                left_sum = 0
                                right_sum = reduce(lambda a, b: a + b, array[i + 1:])
                        elif (i > 0) :
                                left_sum += array[i - 1]
                                right_sum -= array[i]
                        if (left_sum == right_sum) :
                                flag = True
                                break
        
        if (flag == True) : print("YES")
        elif (flag == False) : print("NO")