# =============================================================================
"""
Task
Consider a database table, Emails, which has the attributes First Name and
Email ID. Given N rows of data simulating the Emails table, print
an alphabetically-ordered list of people whose email address ends in @gamil.com.
"""
# =============================================================================
# !/bin/python3

import re

if __name__ == '__main__':
    N = int(input().strip())
    # Dictnory = {}
    lst = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        if re.search('@gmail\.com$', emailID):
            lst.append(firstName)
    print(*sorted(lst), sep='\n')

    #     mail = re.findall('[a-z]+', emailID)
    #     Dictnory[mail[0]] = firstName
    #
    # for i in sorted(Dictnory.values()):
    #     print(i)
# =============================================================================
