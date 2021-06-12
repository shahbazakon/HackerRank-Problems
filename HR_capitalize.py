# =============================================
'''You are asked to ensure that the first and
 last names of people begin with a capital
 letter in their passports. For example,
 alison heck should be capitalised correctly
 as Alison Heck. '''
# =============================================

import math
import os
import random
import re
import sys


# Complete the solve function below.

def solve(s):
    s2 = s.split()
    s3 = ""
    for i in range(0, len(s2)):
        s3 = s3 + s2[i].capitalize() + ' '
    return s3


# ---SECOND METHOD--- #

def solve2(s):
    return s.title()

# ---THIRD METHOD--- #

def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

s = input()
result = solve2(s)
print(result)
# =============================================
