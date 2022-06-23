def print_rangoli(size):
        # your code goes here
        alpha_list = [chr(i) for i in range(ord('a'), ord('a') + size)]
        alpha_list.sort(reverse = True)
        rangoli = []
        for i in range(len(alpha_list)) :
                buff = "-".join(alpha_list[:i + 1:1])
                if (i > 0) :
                        buff += "-" + "-".join(alpha_list[i - 1::-1])
                rangoli.append(buff)
        rangoli += rangoli[-2::-1]
        for line in rangoli :
                pad = ((2 * size) - 1) + (2 * (size - 1)) - len(line)
                pad = int(pad / 2)
                print("-" * pad + line + "-" * pad)

if __name__ == '__main__':
        n = int(input())
        print_rangoli(n)