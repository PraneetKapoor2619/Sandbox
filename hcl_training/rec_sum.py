import sys

def recursive_sum(num):

        if (num == 0):
                return num
        
        result = num + recursive_sum(num - 1)
        return result

print(recursive_sum(int(sys.argv[1])))