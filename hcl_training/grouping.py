from itertools import groupby
string = input()

keys = []
for k, g in groupby(string):
        keys.append(k)
counts = 0
counts_list = []
prev_digit = "-"
for cur_digit in string:
        if cur_digit != prev_digit:
                counts_list.append(counts)
                counts = 0
                prev_digit = cur_digit
        counts += 1
counts_list.append(counts)
counts_list.remove(0)

for i in range(len(keys)):
        print("(" + str(counts_list[i]) + ", " + keys[i] + ")", end = " ")