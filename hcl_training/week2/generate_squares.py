import sys

def generate_squares(num):

        for i in range(num):
                yield i ** 2

print(tuple(generate_squares(int(sys.argv[1]))))