# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.helper(root,0)
    def helper(self,root,val):
        if not root:
            return 0
        val = val*2 + root.val
        if not root.left and not root.right:
            return val
        return self.helper(root.left,val)+self.helper(root.right,val)
