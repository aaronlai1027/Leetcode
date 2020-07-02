# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        self.helper(root,0)
        return self.sum
    def helper(self,root,temp):
        if not root: return
        temp = temp*10 + root.val
        if not root.left and not root.right:
            self.sum += temp
        self.helper(root.left,temp)
        self.helper(root.right,temp)
