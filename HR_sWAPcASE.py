# ========================================================== #
"""You are given a string and your task is to swap cases.
    In other words, convert all lowercase letters to
            uppercase letters and vice versa."""
# ========================================================== #
def swap_case(s):
    str = ""
    for later in s:
        if later == later.upper():
            str += later.lower()
        else:
            str += later.upper()
    return str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
# ========================================================== #
