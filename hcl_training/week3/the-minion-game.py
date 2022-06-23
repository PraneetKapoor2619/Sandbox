def find_substring(string, set_of_substrings):
        count = 0 
        for substring in set_of_substrings :
                index = 0
                while True :
                        index = string.find(substring, index) + 1
                        if (index > 0) :
                                count += 1
                        else :
                                break
        return count

def minion_game(string):
        # use a set so that the slices don't get repeated again and again
        set_of_substrings = {1}
        set_of_substrings.clear()

        for i in range(len(string)) :
                for j in range(len(string) - i) :
                        set_of_substrings.update([string[j:j + i + 1]])
        
        kevin = set(filter(lambda x: x[0] in ['A', 'E', 'I', 'O', 'U'], set_of_substrings))
        stuart = set_of_substrings.difference(kevin)
        
        score_kevin, score_stuart = find_substring(string, kevin), find_substring(string, stuart)
        
        if score_kevin > score_stuart :
                print("Kevin", score_kevin)
        elif score_stuart > score_kevin :
                print("Stuart", score_stuart)
        else :
                print("Draw")


if __name__ == '__main__':
        s = input()
        minion_game(s)