#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a = sorted(a)
    i = 0
    base_index = 0
    base_number = a[0]
    flag = True
    count = 0
    max_count = 0
    while i < len(a):
        if a[i] != a[base_index] and flag:
            base_index = i
            flag = False

        if abs(a[i] - base_number) <= 1:
            count += 1
            max_count = count if max_count < count else max_count
        else:
            i = base_index
            base_number = a[base_index]
            flag = True
            count = 0
            continue

        i += 1

    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
