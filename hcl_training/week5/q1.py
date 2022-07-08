"""
python program to count number of 
        - lines, 
        - words, and
        - characters 
in a text file
"""

print("Opening file1.txt")
fhandle1 = open("file1.txt", 'r')

alllines = ""
for line in fhandle1 :
        alllines += line

line_count = alllines.find(". ")
word_count = len(alllines.split())

# spaces and newlines not considered as characters
reduced_char_count = sum([len(word) for word in alllines.split()])

# everything is considered as a character, even escape sequences
char_count = len(alllines)

print("No. of lines: {:d}\nNo. of words: {:d}".format(line_count, word_count),\
"\nNo. of characters (excluding whitespaces and escape sequences): {:d}".format(reduced_char_count),\
"\nNo. of characters (including whitespaces and escape sequences): {:d}".format(char_count))