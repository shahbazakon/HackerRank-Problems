# ==================================================================================
"""
The height of a binary search tree is the number of edges between the tree's root
and its furthest leaf. You are given a pointer,root , pointing to the root of a binary
search tree. Complete the getHeight function provided in your editor so that it
returns the height of the binary search tree.

 Sample Input:
    7
    3
    5
    2
    1
    4
    6
    7
 Sample Output:
    3
"""


# ==================================================================================
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, Root, data):
        if Root is None:
            return Node(data)
        else:
            if data <= Root.data:
                cur = self.insert(Root.left, data)
                Root.left = cur
            else:
                cur = self.insert(Root.right, data)
                Root.right = cur
        return Root

    def getHeight(self, root):
        # Write your code here
        if root is None:
            return -1
        else:
            l = 1 + self.getHeight(root.left)
            r = 1 + self.getHeight(root.right)
        return max(l, r)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
# ==================================================================================
