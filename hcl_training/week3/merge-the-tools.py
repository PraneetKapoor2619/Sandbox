def merge_the_tools(string, k):
        list_of_compressed_substrings = []
        index = 0
        while index < len(string):
                substring = string[index:index + k]
                buffer = ""
                for char in substring :
                        if not (char in buffer) :
                                buffer += char
                list_of_compressed_substrings.append(buffer)
                index += k
        for compressed_substring in list_of_compressed_substrings :
                print(compressed_substring)

if __name__ == '__main__':
        string, k = input(), int(input())
        merge_the_tools(string, k)