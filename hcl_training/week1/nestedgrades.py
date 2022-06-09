if __name__ == '__main__' :
        records = []
        for _ in range(int(input())) :
                name = input()
                score = float(input())
                records.append([name, score])
        records.sort(key = lambda x: x[0])
        records.sort(key = lambda x: x[1])
        first = records[0][1]
        second = None
        for record in records :
                if (record[1] > first) :
                        if (second is None) :
                                second = record[1]
                        elif (record[1] > second) :
                                break
                        print(record[0])
