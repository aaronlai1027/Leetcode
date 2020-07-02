# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.helper(root1) == self.helper(root2)
    def helper(self,root):
        if not root:
            return []
        if not root.left and not root.right:
            return[root.val]
        l = self.helper(root.left)
        r = self.helper(root.right)
        return l + r
