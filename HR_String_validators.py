# =========================================================================

'''
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.
'''
# =========================================================================
if __name__ == '__main__':
    s = input()
    l = list(s)
    print(l)
    for i in range(0, len(l)):
        if l[i].isalnum():
            print(True)
            break
    else:
        print(False)

    for i in range(0, len(l)):
        if l[i].isalpha():
            print(True)
            break
    else:
        print(False)
    for i in range(0, len(l)):
        if l[i].isdigit():
            print(True)
            break
    else:
        print(False)
    for i in range(0, len(l)):
        if l[i].islower():
            print(True)
            break
    else:
        print(False)
    for i in range(0, len(l)):
        if l[i].isupper():
            print(True)
            break
    else:
        print(False)

# =========================================================================
