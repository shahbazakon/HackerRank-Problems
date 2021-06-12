"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""

if __name__ == '__main__':
    N = int(input())
    lst2 = []
    lst=[]
    for i in range(0, N):
        lst1 = input().split(' ')
        lst2.append(lst1)
    print(lst2)
    for j in range(0, N):
        if(lst2[j][0] =="insert"):
            lst.insert(int(lst2[j][1]), int(lst2[j][2]))
        elif(lst2[j][0] == "print"):
            print(lst)
        elif(lst2[j][0] == "remove"):
            lst.remove(int(lst2[j][1]))
        elif(lst2[j][0] == "append"):
            lst.append(int(lst2[j][1]))
        elif(lst2[j][0] == "sort"):
            lst.sort()
        elif(lst2[j][0] == "pop"):
            lst.pop()
        elif(lst2[j][0] == "reverse"):
            lst.reverse()
        else:
            print("ERROR ! Wrong Input")
