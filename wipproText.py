numberCount, target = map(int, input().split())
c = 0
lst=list(map(int, input().split()))
for j in range(len(lst)):
    if target == c:
        print(str(j-1) + "  " + str(lst[j-1]))
        break
    else:
        c = c + lst[j]