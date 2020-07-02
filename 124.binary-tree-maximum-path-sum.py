# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')
        self.helper(root)
        return self.res
    def helper(self,root):
        if not root: return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.res = max(self.res,root.val+l+r)
        return max(root.val+max(l,r),0)
