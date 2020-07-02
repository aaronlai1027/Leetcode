# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.sum = 0
            self.afterorder(root)
        return root
    
    def afterorder(self,root):
        if not root:
            return
        self.afterorder(root.right)
        self.sum += root.val
        root.val = self.sum
        self.afterorder(root.left)
