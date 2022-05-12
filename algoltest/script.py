GETLINE_BUFFER = input()
num = 80 - len(GETLINE_BUFFER)
while (num):
        GETLINE_BUFFER += '\0'
        num -= 1
flag = 0
count = 0
words = []
for i in range(0, 80):
        words.append(0)
print(len(words))
di = 0
for si in range(0, 80):
        if (GETLINE_BUFFER[si] == '\0'):
                break
        if (GETLINE_BUFFER[si] == ' '):
                flag = 0
                continue
        else:
                if (flag == 0):
                        flag = 1
                        di = 16 * count
                        count += 1
                words[di] = GETLINE_BUFFER[si]
                di += 1
for di in range (0, 80):
        print(di, ":", words[di])