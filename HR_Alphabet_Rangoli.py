#======================================================

"""You are given an integer, . Your task is to print an
 alphabet rangoli of size . (Rangoli is a form of
 Indian folk art based on creation of patterns.)"""
'''
INPUT:
5

OUTPUT:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
#======================================================

def patten(k):
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    lst1 = []
    temp2 = temp1 = k - 1
    symbol = lst[temp1]
    symbol2, symbol1 = symbol, symbol

    M = 2 * k - 1
    N = 4 * k - 3
    for i in range(0, (M // 2) + 1):
        print(symbol.center(N, '-'))
        lst1.append(symbol)
        temp1 = temp1 - 1
        symbol1 = symbol1 + lst[temp1]
        if i != 0:
            temp2 = temp2 - 1
            symbol2 = lst[temp2] + symbol2
        symbol = symbol1 + symbol2

    for i in range(-(M // 2), 0):
        j = (i + 1) * (-1)
        print(lst1[j].center(N, '-'))


if __name__ == '__main__':
    key = int(input())
    patten(key)

#======================================================