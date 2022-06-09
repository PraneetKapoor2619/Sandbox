'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''
if __name__ == '__main__':
        N = int(input())
        array = []
        for i in range(N):
                line = input()
                line = line.split(" ")
                command = line[0]
                if(len(line) == 2 or len(line) == 3):
                        arg1 = int(line[1])
                        if (len(line) == 3):
                                arg2 = int(line[2])
                if (command == "insert"):
                        array.insert(arg1, arg2)
                elif (command == "print"):
                        print(array)
                elif (command == "remove"):
                        array.remove(arg1)
                elif (command == "append"):
                        array.append(arg1)
                elif (command == "sort"):
                        array.sort()
                elif (command == "pop"):
                        array.pop()
                elif (command == "reverse"):
                        array = array[::-1]