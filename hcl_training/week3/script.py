aList = [1,2]
bList = [3,4]

kvps = { '1' : aList, '2' : bList }
theCopy = kvps.copy()

kvps['1'][0] = 5

sum = kvps['1'][0] + theCopy['1'][0]
print(sum)
