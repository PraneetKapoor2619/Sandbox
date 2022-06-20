def mutate_string(string, position, character):
        str_arr = list(string)
        str_arr[position] = character
        return "".join(str_arr)

if __name__ == '__main__':
        s = input()
        i, c = input().split()
        s_new = mutate_string(s, int(i), c)
        print(s_new)