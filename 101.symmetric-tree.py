# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.preorder(root.left,root.right)
    def preorder(self, n1 ,n2):
        if not n1 or not n2:
            return n1 == n2
        if n1.val != n2.val:
            return False
        left = self.preorder(n1.left,n2.right)
        right = self.preorder(n1.right,n2.left)
        return left and right
