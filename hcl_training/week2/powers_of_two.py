import sys

def power_of_two():

        index = 0
        while True:
                yield 2 ** index
                index += 1


gen = power_of_two()

count = 0
for i in gen:

        if count >= int(sys.argv[1]):
                break
        else:
                print(i)
                count += 1