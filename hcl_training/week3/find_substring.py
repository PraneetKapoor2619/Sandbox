def count_substring(string, sub_string):
        count = 0
        index = 0
        s_index = 0
        
        while (index < len(string)) :
                s_index = string[index:].find(sub_string)
                if (s_index >= 0) :
                        index += s_index + len(sub_string) - 1
                        count += 1
                else :
                        break
        
        return count 
                        


if __name__ == '__main__':
        string = input().strip()
        sub_string = input().strip()

        count = count_substring(string, sub_string)
        print(count)