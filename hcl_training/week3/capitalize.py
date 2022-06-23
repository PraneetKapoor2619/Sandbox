#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
        new_str = ""
        inside_word = False
        for char in s :
                if (char.isalnum()) :
                        if (inside_word == False) :
                                inside_word = True
                                new_str += char.upper()
                        else :
                                new_str += char
                else :
                        inside_word = False
                        new_str += char
        return new_str

if __name__ == '__main__':
        s = input()

        result = solve(s)
        print(result)