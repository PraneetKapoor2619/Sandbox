LBA = 0
while (True):
        LBA = int(input())
        C = int(LBA / (2 * 18))
        H = int((LBA / 18) % 2)
        S = int((LBA % 18) + 1)
        print("C:", C, "H:", H, "S:", S)