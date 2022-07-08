"""
Write a python program to read all strings from a text file and display them.
"""

fhandle = open("file1.txt", 'r')

string = fhandle.readline()
while string :
        print(string, end = "")
        string = fhandle.readline()