import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5 and n % 2 == 0:
            print("Not Weird")
        elif 6 <= n <= 20 and n % 2 == 0:
            print("Weird")
        else:
            print("Not Weird")