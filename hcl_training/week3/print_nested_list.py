l = [1, 2, 3, [1, 2, 3]]
for i in l:
    if (type(i) == list) :
        for j in i :
            print(j)
    else :
        print(i)
