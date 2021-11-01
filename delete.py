
inputStr = input("Enter String : ")
temp = inputStr
char = list(set(inputStr))
print (char)
count = 0
for j in range(len(inputStr)):
    for i in range(len(char)):
        lst = list(inputStr)
        lst.insert(j, char[i])
        lst.remove(inputStr[1-i])
        NewStr = "".join(lst)
        print(NewStr)
        if NewStr == NewStr[::-1]:
            if NewStr != temp:
                count = count + 1
            # print(NewStr)
        else:
            continue
        inputStr = temp
print("possible PALINDROME " + str(count))




