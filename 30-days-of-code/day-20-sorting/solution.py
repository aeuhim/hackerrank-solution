#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numSwaps = 0
    for idx in range(n-1):
        state = numSwaps
        for jdx in range(n-1-idx):
            if a[jdx] > a[jdx+1]:
                a[jdx], a[jdx+1] = a[jdx+1], a[jdx]
                numSwaps += 1
        if state == numSwaps:
            break
    print("Array is sorted in %d swaps." % numSwaps)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])
    