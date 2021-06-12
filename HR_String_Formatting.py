# ==========================================================================#
'''
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order
specified above for each  from  to .
Each value should be space-padded to match the width of the binary value of .
'''


# ==========================================================================#
def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        Decimal = str(i)
        Octal = str(oct(i))[2:]
        Hexadecimal = str(hex(i))[2:]
        Binary = str(bin(i))[2:]
        Format = Decimal+" "+Octal+" "+Hexadecimal+" "+Binary+"\n"
        print(Format)
    return


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
# ==========================================================================#
