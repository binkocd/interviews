#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    low, high = scores[0], scores[0]
    maxlow, maxhigh = 0, 0
    for i in scores:
        if i > high:
            high = i
            maxhigh += 1
        elif i < low:
            low = i
            maxlow += 1
    return maxhigh, maxlow


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
