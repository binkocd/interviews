#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Sort socks
    ar.sort()
    matching_pairs = 0
    sorts = {}
    # Pair socks
    for i in range(0, len(ar)):
        if ar[i] in sorts:
            sorts[ar[i]] += 1
        else:
            sorts[ar[i]] = 1

    for x in sorts:
        matching_pairs += sorts[x] // 2

    return matching_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
