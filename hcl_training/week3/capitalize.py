#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
        splits = s.split()
        splits = [string.capitalize() for string in splits]
        result = " ".join(splits)
        return result



if __name__ == '__main__':
        s = input()

        result = solve(s)
        print(result)