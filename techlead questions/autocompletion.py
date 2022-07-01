import re

a = input("")
word_list = ["dog", "dark", "cat", "door", "dodge"]
poss = []

for word in word_list:
    if (word[:len(a)] == a):
        poss.insert(len(poss), word)
print(poss)
