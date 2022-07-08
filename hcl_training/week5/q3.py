fhandle = open("file1.txt", 'r')

string = fhandle.readline()
while string :
        print(string, end = "")
        string = fhandle.readline()