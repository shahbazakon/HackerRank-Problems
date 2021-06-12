# ================================================
"""
collections.Counter()
A counter is a container that stores elements
as dictionary keys, and their counts are
stored as dictionary values.
"""
# ================================================
import collections

numShoes = int(input())                                     # No. of Shoes that i have
Shoes = collections.Counter(map(int, input().split(' ')))   # Size of Shoes tha i have
numCost = int(input())                                      # No. of shoes that customer Wants to buy
add = 0
for i in range(numCost):
    S, P = map(int, input().split(" "))                     # Take the Size and prise of Shoes
    if Shoes[S]:                                            # Match the Shoes Size
        add = add + P                                       # Creating the bill
        Shoes[S] = Shoes[S] - 1                             # remove the Shoes size form initial collection
print(add)

# ================================================
