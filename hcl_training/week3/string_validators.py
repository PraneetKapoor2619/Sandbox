if __name__ == '__main__':
        s = input()
        results = [False] * 5
        for char in s:
                if char.isalnum() :
                        if (results[0] == False) :
                                results[0] = True
                        if (char.isalpha()) :
                                if (results[1] == False) :
                                        results[1] = True
                                if (char.islower() and results[3] == False) :
                                        results[3] = True
                                elif (char.isupper() and results[4] == False) :
                                        results[4] = True
                        elif (char.isdigit() and results[2] == False) :
                                results[2] = True
        for r in results:
                print(r)