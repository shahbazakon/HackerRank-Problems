# ========================================================================#
'''
Mr. Vincent works in a door mat manufacturing company. One day,
he designed a new door mat with the following specifications:

Mat size must be M X.N ( N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''


# ========================================================================#
def Door_Mat(M, N):
    Str = 'WELCOME'
    symbol = '.|.'
    val = 1
    flag = 0
    for i in range(0, M):
        if i == M // 2:
            print(Str.center(N, '-'))
            flag = 1
        else:
            print(symbol.center(N, '-'))

        symbol = '.|.'

        if flag == 1:
            val = val - 2
            for j in range(val - 1):
                symbol = symbol + '.|.'

        else:
            val = val + 2
            for j in range(val - 1):
                symbol = symbol + ".|."


if __name__ == '__main__':
    Height, width = input().split(" ")
    Door_Mat(int(Height), int(width))

# ========================================================================#
