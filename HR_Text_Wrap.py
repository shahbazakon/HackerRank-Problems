# ==========================================================#
"""
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.
"""
# ==========================================================#
import textwrap


def wrap(String, Max_Width):
    l = list(String)
    nothing = ''
    num = Max_Width
    for i in range(0, (len(String) // num) + 1):
        l.insert(num, '\n')
        num = num + Max_Width + 1
    return nothing.join(l)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
# ==========================================================#
