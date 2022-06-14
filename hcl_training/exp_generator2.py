def generator():
        num = 1
        print("->", num)
        yield num

        num += 1
        print("->", num)
        yield num

        num += 1
        print("->", num)
        yield num

g = generator()
while(next(g)):
        x = None