# ==================================================================#
"""
Task
Given 2 sets of integers, M and N, print their symmetric difference
 in ascending order. The term symmetric difference indicates
 those values that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order,
one per line.

"""
# ==================================================================#

s1 = int(input())
a = map(int, input().split())
set1 = set(a)
s2 = int(input())
b = map(int, input().split())
set2= set(b)
diff1 = list(set2.difference(set1))
diff2 = list(set1.difference(set2))
mylist = diff1 + diff2
mylist.sort()
for i in range(0,len(mylist)):
     print(mylist[i])


# ==================================================================#
