def closestNumbers(numbers):
        numbers.sort()

        dict_of_indices = {}
        
        for i in range(len(numbers)) :
                for j in range(i, len(numbers)) :
                        diff = abs(numbers[i] - numbers[j])
                        if (diff == 0) : continue
                        if (dict_of_indices.get(diff) == None) :
                                dict_of_indices[diff] = [(i, j)]
                        else :
                                val = dict_of_indices[diff]
                                val.append((i, j))
        for k, v in dict_of_indices.items() :
                for tup in v :
                        print(tup[0], tup[1])
                return 0



if __name__ == "__main__" :
        numbers_count = int(input().strip())

        numbers = []

        for _ in range(numbers_count) :
                numbers_item = int(input().strip())
                numbers.append(numbers_item)
        
        closestNumbers(numbers)