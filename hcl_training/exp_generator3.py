def generator():
        num = 1
        while(num <= 10):
                print("->", num)
                num += 1
                yield num

g = generator()
while(next(g)):
        x = None