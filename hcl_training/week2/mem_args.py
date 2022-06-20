def func(a, l = []):
        print(id(l))
        l = []
        l.append(a)
        print(id(l), l)

func(1)
func(2)
func(3)