def BinarySearch(sorted_list, key):
        min_index = 0
        max_index = len(sorted_list) - 1

        while (min_index <= max_index) :

                mid_index = (min_index + max_index) // 2

                if sorted_list[mid_index] == key :
                        return mid_index

                elif sorted_list[mid_index] < key :
                        min_index += 1
                
                else :
                        max_index -= 1
        
        return -1

if __name__ == "__main__" :
        list = sorted([1, 41, 56, 74, 89, 21, 34, 57, 88, 99])

        print("Key: {:d}, Index: {:d}".format(34, BinarySearch(list, 34)))
        print("Key: {:d}, Index: {:d}".format(56, BinarySearch(list, 56)))
        print("Key: {:d}, Index: {:d}".format(51, BinarySearch(list, 51)))