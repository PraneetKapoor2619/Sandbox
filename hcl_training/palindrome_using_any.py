def isPallindrome(number):
        if int(number) >= 0:
                for i in range(len(number)):
                        if (number[i] != number[len(number) - i - 1]):
                                return False
                return True
        else:
                print(False)
                exit()
                                
N, string = int(input()), input().split(" ")
for i in range(len(string)):
        string[i] = isPallindrome(string[i])
print(any(string))