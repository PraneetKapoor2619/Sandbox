import math
import re
import sys

N = int(sys.stdin.readline())
istring = sys.stdin.readline()
p = [2, 3, 5, 7]
pdict = { 0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
emotions = [10 if e == "Happy" else (5 if e == "Sad" else (2 if e == "Neutral" else 1)) for e in re.findall("[a-zA-Z]+", sys.stdin.readline())]
score1 = sum([e*int(i) for e,i in zip(emotions, re.findall("[0-9]+", istring))])
vowels = [len(re.findall("[aeiouAEIOU]", w)) for w in re.findall("[a-zA-Z]+", istring)]
score2 = sum([v * int(n) for v,n in zip(vowels, re.findall("[0-9]+", istring))])
if(score1 >= score2): area = math.floor(score1 / score2)
else: area = math.floor(score2 / score1)
if(p.__contains__(area)): print("Yes", pdict.get(area), end="")
else: print("No", pdict.get(area), end="")