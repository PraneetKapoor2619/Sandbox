def func(a, b, c, *args, **kargs):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("*args =", args)
        print("2nd star args =", args[1])
        print("**kwargs =", kargs)
        key_list = list(kargs.keys())
        print("2nd kwargs =", kargs[key_list[1]])

func(1, 2, 3, 10, 20, 30, alpha = 100, beta = 200, gamma = 300)