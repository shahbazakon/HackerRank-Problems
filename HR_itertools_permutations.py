# ============================================================================
"""
itertools.permutations(iterable[, r])

This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable,
 and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So,
if the input iterable is sorted,
the permutation tuples will be produced in a sorted order.
"""
# ============================================================================

from itertools import permutations

S, N = input().split(' ')

List1 = list(permutations(S, int(N)))
List2 = []
for i in range(len(List1)):
    concat = ""
    for j in range(len(List1[i])):
        concat = concat + List1[i][j]
    List2.append(concat)
List2.sort()
for i in range(len(List2)):
    print(List2[i])
# ============================================================================
