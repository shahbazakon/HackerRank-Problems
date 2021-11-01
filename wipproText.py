numberCount, target = map(int, input().split())
count = 0
lst=list(map(int, input().split()))
for j in range(len(lst)):
    if target == count:
        print(str(j-1) + "  " + str(lst[j-1]))
        break
    else:
        count = count + lst[j]