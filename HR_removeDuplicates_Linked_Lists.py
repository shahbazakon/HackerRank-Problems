# ================================================================================
"""
Task
A Node class is provided for you in the editor. A Node object has an integer data
field,data , and a Node instance pointer,next , pointing to another node
(i.e.: the next node in a list).

A removeDuplicates function is declared in your editor, which takes a pointer to
the head node of a linked list as a parameter. Complete removeDuplicates so that it
deletes any duplicate nodes from the list and returns the head of the updated list.

Note: The head pointer may be null, indicating that the list is empty. Be sure to reset
your next pointer when performing deletions to avoid breaking the list.

Sample Input:
6
1
2
2
3
3
4

Sample Output:
1 2 3 4
"""


# ================================================================================
class Node:
    def __init__(self, Data):
        self.data = Data
        self.next = None


def removeDuplicates(Head):
    current = Head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return Head


def display(Head):
    current = Head
    while current:
        print(current.data, end=' ')
        current = current.next


def insert(Head, Data):
    p = Node(Data)
    if Head is None:
        Head = p
    elif Head.next is None:
        Head.next = p
    else:
        start = Head
        while start.next is not None:
            start = start.next
        start.next = p
    return Head


class Solution:
    pass


Lst = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = insert(head, data)
head = removeDuplicates(head)
display(head)
# ================================================================================
