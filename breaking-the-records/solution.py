#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_score = float("-inf")
    min_score = float("inf")
    max_ctr = -1
    min_ctr = -1
    records = []
    for score in scores:
        if max_score < score:
            max_score = score
            max_ctr += 1
        if min_score > score:
            min_score = score
            min_ctr += 1
    record = [max_ctr, min_ctr]
    return record

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
