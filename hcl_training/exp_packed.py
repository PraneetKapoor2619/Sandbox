def func(lst):
        print(lst)
        return lst

arr = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
print(*func(arr), sep = "\n")