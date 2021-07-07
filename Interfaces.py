# ===========================================================================
"""
Task:
The AdvancedArithmetic interface and the method declaration for the abstract
divisorSum(n) method are provided for you in the editor below.
Complete the implementation of Calculator class, which implements the
AdvancedArithmetic interface. The implementation for the divisorSum(n) method
must return the sum of all divisors of n.

Example:
    n = 25
    The divisors of 25 are 1,5,25. Their sum is 31.
"""
# ===========================================================================
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n==1:
            return 1
        else:
            s= n + 1
            for i in range(2,n//2+1):
                if(n%i==0):
                    s = s+i
            return s


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
# ===========================================================================
