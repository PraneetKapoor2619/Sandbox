def split_and_join(line):
        # write your code here
        str_arr = line.split(" ")
        joined_str = "-"
        joined_str = joined_str.join(str_arr)
        return joined_str

if __name__ == '__main__':
        line = input()
        result = split_and_join(line)
        print(result)