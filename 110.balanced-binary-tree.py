# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.isBalanced = True
        self.helper(root)
        return self.isBalanced
        
    def helper(self,root):
        if not root: return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        if abs(l-r)>1:
            self.isBalanced = False
        return max(l,r)+1
