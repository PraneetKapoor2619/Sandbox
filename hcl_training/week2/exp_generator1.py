def generator():

        print("-> 1")
        yield 1

        print("-> 2")
        yield 2

        print("-> 3")
        yield 3
        
        print("-> 4")
        yield 4

g = generator()
while(next(g)):
        print("We will go on...")