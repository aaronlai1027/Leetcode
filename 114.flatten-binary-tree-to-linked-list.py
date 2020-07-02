# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.tranverse(root)
        
    def tranverse(self,root):
        if not root:
            return
        self.tranverse(root.right)
        self.tranverse(root.left)
        
        root.right = self.pre
        root.left = None
        self.pre = root
