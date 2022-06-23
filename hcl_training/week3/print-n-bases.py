def print_formatted(number):
        # your code goes here
        pad = len("{0:b}".format(number))
        for i in range(1, number + 1) :
                print("{0:d}".format(i).rjust(pad) + " " + "{0:o}".format(i).rjust(pad) + " " + "{0:X}".format(i).rjust(pad) + " " + "{0:b}".format(i).rjust(pad))
 
if __name__ == '__main__':
        n = int(input())
        print_formatted(n)