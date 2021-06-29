# ============================================================
"""
Given a base-10 integer,n , convert it to binary (base-2).
Then find and print the base- integer denoting the
maximum number of consecutive 1's in n's binary representation.
When working with different bases, it is common to show
the base as a subscript.
"""
# ============================================================
import math
import os
import random
import re
import sys


def maxConsecutiveOnes(n):
    n = bin(n)
    n = n[2:]
    print(max(map(len, n.split('0'))))


if __name__ == '__main__':
    n = int(input().strip())
    maxConsecutiveOnes(n)

# ============================================================
