# ===============================================================================
"""
itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
"""

# ===============================================================================

from itertools import product

A = tuple(map(int, input().split(' ')))
B = tuple(map(int, input().split(' ')))

lst = list(product(A,B))
sum = ""
for i in lst:
    sum = sum + str(i)+ " "
print(sum)

# ===============================================================================
