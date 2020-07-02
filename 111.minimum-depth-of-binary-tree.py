# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.helper(root)
    def helper(self,root):
        if not root: return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l == 0 or r == 0:
            return l + r + 1
        return min(l,r)+1
