# =================================================================
"""
Task

You are given two values a and b.
Perform integer division and print a/b.

Input Format

The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.
"""


# =================================================================
def div(a, b):
    try:
        print(int(int(a) / int(b)))
    except ZeroDivisionError as e:
        print("Error Code:", "integer division or modulo by zero")
    except ValueError as v:
        print("Error Code:", v)


N = int(input())
lst1 = []
lst2 = []
for i in range(N):
    a, b = input().split()
    lst1.append(a)
    lst2.append(b)

for j in range(N):
    div(lst1[j], lst2[j])
# =================================================================
