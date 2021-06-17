# =========================================================================
"""
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container,
but the only difference is that a defaultdict will have a default value
if that key has not been set yet. If you didn't use a defaultdict you'd
have to check to see if that key exists, and if it doesn't,
set it to what you want.

Output Format

Output m lines.
The ith line should contain the 1-indexed positions of the occurrences of
the ith word separated by spaces.
"""
# =========================================================================

from collections import defaultdict
d=defaultdict(list)
lst=[]
a , b = map(int,input().split())

for i in range(0,a):
    d[input()].append(i+1)

for i in range(0,b):
    lst = lst + [input()]

for i in lst:
    if i in d:
        print(" ".join(map(str,d[i])))
    else:
        print("-1")

# =========================================================================
