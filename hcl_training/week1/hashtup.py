if __name__ == '__main__':
        n = int(input())
        arguments = input()
        integer_list = [int(x) for x in arguments.split(" ")]
        tup = tuple(integer_list)
        print(hash(tup))