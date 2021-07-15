# ==============================================================================
"""
Your local library needs your help! Given the expected and actual return dates
for a library book, create a program that calculates the fine (if any).
The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine
will be charged (i.e.: fine=0).

2. If the book is returned after the expected return day but still within the
same calendar month and year as the expected return date,
fine= 15Hackos x (the number of days late).

3. If the book is returned after the expected return month but still within the
same calendar year as the expected return date, the
fine= 500Hackos x (the number of months late).

4. If the book is returned after the calendar year in which it was expected
10000 Hackos,
there is a fixed fine of .

Sample Input:

STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)

Sample Output:

45

"""
# ==============================================================================
d1, m1, y1 = map(int, input().split())  # returned
d2, m2, y2 = map(int, input().split())  # due
fine = 0
if d1 > d2:
    fine = 0
    fine = 15 * (d1 - d2)

if m1 > m2 and y1 == y2:
    fine = 0
    fine = 500 * (m1 - m2)

if m1 < m2 and y1 == y2:
    fine = 0

if y1 > y2:
    fine = 0
    fine = 10000
if y1 < y2:
    fine = 0

print(fine)  # fine

# ==============================================================================
