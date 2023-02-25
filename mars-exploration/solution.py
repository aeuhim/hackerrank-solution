#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    change_counter = 0
    for idx, char in enumerate(s):
        part_idx = idx % 3
        if part_idx == 0 and char != "S":
            change_counter += 1
        if part_idx == 1 and char != "O":
            change_counter += 1
        if part_idx == 2 and char != "S":
            change_counter += 1
    return change_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
