# ==========================================================================#
"""You are given N , you need to print the number of position
                where digits exactly divides N."""
# ==========================================================================#
lst = []
N = int(input("Enter Digits and '0' To Terminate:\n"))
while True:
    if N == 0:
        break
    else:
        lst.append(N)
        N = int(input())

for i in range(0, len(lst)):

    if int(len(lst) % lst[i]) == 0:
        print("The list is divided by", lst[i], "that's position is ", i)
        # break
else:
    print("The element is not present in list which devided whole list")
# ==========================================================================#
