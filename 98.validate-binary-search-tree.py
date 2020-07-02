# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root,-float('inf'),float('inf'))
        
    def helper(self,root,lowerbound,upperbound):
        if not root:
            return True
        if root.val <= lowerbound or root.val >=upperbound:
            return False
        left = self.helper(root.left,lowerbound,root.val)
        right = self.helper(root.right,root.val,upperbound)
        return left and right
        
