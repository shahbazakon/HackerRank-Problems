# =================================================================== #
"""
A set is an unordered collection of elements
without duplicate entries.
When printed, iterated or converted into a sequence,
its elements will appear in an arbitrary order.

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns

float: the resulting float value rounded to 3 places after the decimal
Input Format

The first line contains the integer, N, the size of arr.
The second line contains the N space-separated integers arr[i],
"""


# =================================================================== #

def average(array):
    # your code goes here
    NEWset =set(array)
    array = list(NEWset)
    s = sum(array)
    n = len(array)

    return s / n


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# =================================================================== #
