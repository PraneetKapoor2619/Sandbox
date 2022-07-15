import re

S = input()

# perform regex search here
vowels = "aeiouAEIOU"
consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

match_list = re.findall(r"(?<=[%s])([%s]{2,}(?=[%s]))" % (consonants, vowels, consonants), S)

if len(match_list) :
        for match in match_list :
                print(match)

else :
        print(-1)