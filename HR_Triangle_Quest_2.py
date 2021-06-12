# ===================================================== #
"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321
"""
# ===================================================== #
end = ""
start = ""
for i in range(1, int(input()) + 1):
    end = str(i) + end
    start = start + str(i)
    print(start + end[1:])

# OTHER SOLUTION
"""
for i in range(1, int(input()) + 1):
    print(((10**i - 1)//9)**2)
"""
# ===================================================== #
