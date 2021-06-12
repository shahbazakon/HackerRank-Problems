# =================================================================#

'''
    In this challenge, the user enters a string and a substring.
    You have to print the number of times that the substring
    occurs in the given string.
    String traversal will take place from left to right,
    not from right to left.
'''


# =================================================================#
def count_substring(string, sub_string):
    string_size = len(string)
    substring_size = len(sub_string)
    mycount = 0
    for i in range(0, string_size - substring_size + 1):
        if string[i:i + substring_size] == sub_string:
            mycount += 1
    return mycount


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    sub_count = count_substring(string, sub_string)
    print(sub_count)
# =================================================================#
