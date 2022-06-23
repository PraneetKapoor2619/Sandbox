import copy

def shallow_copy1(arr_p):
        print(id(arr_p), id(arr_p[0]))
        arr_p[0] = [10, 20, 30]
        print(id(arr_p[0]))

def shallow_copy2(arr_p):
        print(id(arr_p), id(arr_p[0]))
        arr_p[0][1] = 455

def deep_copy1(arr_p):
        print(id(arr_p), id(arr_p[0]))
        arr_p[0][1] = 2


def deep_copy2(arr_p):
        print(id(arr_p), id(arr_p[0]))
        arr_p[0][1] = 2

arr = [[1, 2, 3], [4, 5, 6]]
print(id(arr), id(arr[0]))
shallow_copy1(copy.copy(arr))
print(arr)
shallow_copy2(copy.copy(arr))
print(arr)
deep_copy1(copy.deepcopy(arr))
print(arr)
deep_copy2([x[:] for x in arr])
print(arr)