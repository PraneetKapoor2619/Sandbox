def simple_func(number):
        x = number + 256
        print(id(x), "->", x)

def main_func(number):
        x = number
        def func(y):
                y = x + 256
                print(id(x), "->", y)
        return func
  
simple_func(10)
simple_func(5)

ten = main_func(10)
five = main_func(5)
del(main_func)
ten(0)
five(0)