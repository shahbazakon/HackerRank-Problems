import math
Num1 = int(input("Enter Any Number "))
Num = Num1
B=0
temp = str(Num1)
power = len(temp)
for i in range(0,power):
        Rem = Num%10
        A = Rem**power
        B = A + B
        Num = Num//10
if(B==Num1):
        print("It's a Armtrong Number")
else:
        print("Not Armstrong Number")