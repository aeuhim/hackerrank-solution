#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s_stripped = s[:-2]
    hour_prepared = int(s_stripped[:2]) % 12
    if s[-2] == "P":
        hour_prepared += 12
    hour_militarized = str(hour_prepared).zfill(2)
    result = hour_militarized + s_stripped[2:]
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
