#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    bird_sights = {}
    max_sight_count = 0
    lowest_id = 0
    for bird in arr:
        if bird not in bird_sights:
            bird_sights[bird] = 1
            continue
        bird_sights[bird] += 1
        if max_sight_count > bird_sights[bird]:
            continue
        if max_sight_count < bird_sights[bird]:
            max_sight_count = bird_sights[bird]
            lowest_id = bird
            continue
        if lowest_id > bird:
            lowest_id = bird
    return lowest_id

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
