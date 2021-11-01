'''
You are given a string S consisting of lowercase a-z
All the characters in the sting that occur 2, 3, 5, 7, 11 etc(prime numbers)
number of times are considered to be special.
You have to remove all the special characters and form a new string P
if the new string formed is empty she assumes P as MARY

TasK: Determine the string P for the given string S.

INPUT: aabbbbcc
output : bbbb

Explanation: a.c occurs prime number of time, so yoyu have to remove these.


'''

# Write your code here
def SieveOfEratosthenes(prime, n) :

    # Initialize all entries in
    # prime[] as true
    for i in range(n + 1) :
        prime[i] = True

    # Initialize 0 and 1 as non prime
    prime[0] = prime[1] = False

    # Traversing the prime array
    i = 2
    while i*i <= n :

        # If i is prime
        if (prime[i] == True) :

            # All multiples of i must
            # be marked false as they
            # are non prime
            j = 2
            while i*j <= n :
                prime[i * j] = False
                j += 1
        i += 1

# Function to remove characters which
# have prime frequency in the String
def removePrimeFrequencies(s) :

    # Length of the String
    n = len(s)

    # Create a bool array prime
    prime = [False] * (n + 1)

    # Sieve of Eratosthenes
    SieveOfEratosthenes(prime, n)


    # Stores the frequency of character
    m = {}


    for i in range(len(s)) :
        if s[i] in m :
            m[s[i]]+= 1
        else :
            m[s[i]] = 1
    new_String = ""
    for i in range(len(s)) :

        if (prime[m[s[i]]]) :
            continue
        new_String += s[i]
    if(len(new_String)==0):
        print("MARY")
    else:
        print(new_String)


num = int(input())
lst=[]
for i in range(num):
    lst.append(input())

for j in range(len(lst)):
    removePrimeFrequencies(list(lst[j]))

