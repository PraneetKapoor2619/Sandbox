def func1(arr_p):
        print(id(arr_p))
        arr_p[0] = 12

arr = [1, 2, 3, 4]
arr_1 = arr
print(id(arr))
print(id(arr_1))
func1(arr)
print(arr, arr_1)