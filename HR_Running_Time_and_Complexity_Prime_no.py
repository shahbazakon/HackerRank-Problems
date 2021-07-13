# ==================================================================================
"""
Task
A prime is a natural number greater than  that has no positive divisors
other than  and itself. Given a number, , determine and print whether it
 is Prime or Not Prime.

Note: If possible, try to come up with a 0(sqrt(n)) primality algorithm, or see what
sort of optimizations you come up with for an 0(n) algorithm. Be sure to check
out the Editorial after submitting your code.
"""
# ===================================================================================

"""
#Not work on very large value.
def isPrime(n):
    if n is 1:
        return print("Not prime")
    elif n < 0:
        -n

    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag = 1
    if flag is 1:
        print("Not prime")
    else:
        print("Prime")


T = int(input())
Lst = []
for j in range(T):
    Lst.append(int(input()))

for k in range(T):
    isPrime(Lst[k])
"""

for _ in range(int(input())):
    num = int(input())
    if num == 1:
        print("Not prime")
    else:
        if num % 2 == 0 and num > 2:
            print("Not prime")
        else:
            for i in range(3, int(num**(1/2))+1, 2):
                if num % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")
# ===================================================================================
