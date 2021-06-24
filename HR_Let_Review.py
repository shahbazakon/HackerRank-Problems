# =========================================================
"""
Objective
Today we will expand our knowledge of strings, combining
it with what we have already learned about loops.
Check out the Tutorial tab for learning materials and an
instructional video.
"""
# =========================================================
# Enter your code here. Read input from STDIN. Print output
# to STDOUT

def Review(mystring):
    mylst = []
    evenstr = ""
    oddstr = ""
    for i in range(len(mystring)):
        mylst.append(mystring[i])
    for j in range(len(mylst)):
        if j % 2 == 0:
            evenstr += mylst[j]
        else:
            oddstr += mylst[j]
    print(evenstr + " " + oddstr)


lst = []
for i in range(int(input())):
    lst.append(input())
for i in range(len(lst)):
    Review(lst[i])
# =========================================================
