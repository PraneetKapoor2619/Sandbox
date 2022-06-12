import sys

def generate_even_numbers(terms):

        count = 0
        while(count < 2 * terms):
                yield count
                count += 2

g = generate_even_numbers(int(sys.argv[1]))
print(list(g))