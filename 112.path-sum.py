# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        return self.helper(root,0,sum)
        
    def helper(self,root,tot,sum):
        if not root: return False
        tot = tot + root.val
        if not root.left and not root.right and tot == sum: return True
        l = self.helper(root.left,tot,sum)
        r = self.helper(root.right,tot,sum)
        return l or r
