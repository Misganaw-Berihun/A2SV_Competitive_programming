#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    prices.sort()

    total = 0
    i = 0
    
    for val in prices:
        total += val
        if total <= k:
            i += 1
        else:
            break
    
    return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = map(int, raw_input().rstrip().split())

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()